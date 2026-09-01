#!/usr/bin/env python3
"""Pull today's Binance BTCUSDT perp basis (mark vs index). Append-only.

Auto (no args): uses today's QMI row. Manual: pass --z from the chart.
"""

import argparse
import csv
import json
import os
import ssl
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def https_context() -> ssl.SSLContext:
    paths = ssl.get_default_verify_paths()
    for candidate in (paths.cafile, paths.openssl_cafile, "/etc/ssl/cert.pem"):
        if candidate and Path(candidate).exists():
            return ssl.create_default_context(cafile=candidate)
    return ssl.create_default_context()


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "trading" / "basis.csv"
MARK_URL = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT"
SOURCE = "fapi.binance.com BTCUSDT perp"
FIELDS = ["date", "mark", "index", "basis_usd", "basis_pct", "z", "source"]
HEADERS = {"User-Agent": "Quant-Blocks-BTC/0.1"}
QMI_METRICS = Path(
    os.environ.get(
        "QMI_METRICS",
        str(
            Path.home()
            / "Quantitative-Macro-Intelligence"
            / "04-Quant-Models"
            / "chaos-corridor"
            / "data"
            / "chaos_corridor_metrics.csv"
        ),
    )
)


def get(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20, context=https_context()) as resp:
        return json.load(resp)


def qmi_today() -> dict:
    if not QMI_METRICS.exists():
        sys.exit("QMI CSV missing — run corridor first")
    with QMI_METRICS.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("QMI CSV empty — run corridor first")
    row = rows[-1]
    day = (row.get("Date") or "").split("T")[0]
    today = datetime.now(timezone.utc).date().isoformat()
    if day != today:
        sys.exit(f"QMI last row is {day}, today is {today} — run corridor first")
    return row


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--z", help="Optional. Z from the chart.")
    args = parser.parse_args()

    qmi = qmi_today()
    z = args.z if args.z else f"{float(qmi['Z_Score']):.2f}"
    print(f"QMI {qmi.get('Date', '')}  Z={z}")

    px = get(MARK_URL)
    mark = float(px["markPrice"])
    index = float(px["indexPrice"])
    day = datetime.fromtimestamp(int(px["time"]) / 1000, tz=timezone.utc).date().isoformat()
    basis_usd = mark - index
    basis_pct = (mark / index - 1) * 100 if index else 0.0

    row = {
        "date": day,
        "mark": round(mark, 2),
        "index": round(index, 2),
        "basis_usd": round(basis_usd, 2),
        "basis_pct": round(basis_pct, 4),
        "z": z,
        "source": SOURCE,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    existing = set()
    if OUT.exists():
        with OUT.open(newline="") as f:
            existing = {r["date"] for r in csv.DictReader(f)}

    if day in existing:
        print(f"already have {day}: skip")
        return

    write_header = not OUT.exists()
    with OUT.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)
    print(f"appended {row}")


if __name__ == "__main__":
    main()
