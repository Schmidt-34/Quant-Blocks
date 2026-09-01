#!/usr/bin/env python3
"""Pull today's Binance BTCUSDT perp OI. Append-only to trading/oi.csv.

Auto (timer or no args): uses today's full QMI row (join on date).
Manual: pass --z from the chart. Same script.
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
OUT = ROOT / "trading" / "oi.csv"
OI_URL = "https://fapi.binance.com/fapi/v1/openInterest?symbol=BTCUSDT"
MARK_URL = "https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT"
HIST_URL = "https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1d&limit=2"
SOURCE = "fapi.binance.com BTCUSDT perp"
FIELDS = ["date", "oi_usd", "oi_24h_pct", "z", "source"]
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
    """Full today's corridor row. Future models join QMI CSV to oi.csv on date."""
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
    parser.add_argument(
        "--z",
        help="Optional. Z from the chart. If omitted, uses today's QMI row.",
    )
    args = parser.parse_args()

    qmi = qmi_today()
    z = args.z if args.z else f"{float(qmi['Z_Score']):.2f}"
    print(
        f"QMI {qmi.get('Date', '')}  Z={z}  "
        f"spot={qmi.get('Close')}  trend={qmi.get('Fair_Value')}  "
        f"risk={qmi.get('Risk_Score')}  "
        f"(full corridor row stays in QMI CSV; join to oi.csv on date)"
    )

    live = get(OI_URL)
    mark_row = get(MARK_URL)
    hist = get(HIST_URL)

    day = datetime.fromtimestamp(live["time"] / 1000, tz=timezone.utc).date().isoformat()
    oi_usd = float(live["openInterest"]) * float(mark_row["markPrice"])

    prev_usd = None
    for bar in hist:
        bar_day = datetime.fromtimestamp(int(bar["timestamp"]) / 1000, tz=timezone.utc).date().isoformat()
        if bar_day != day:
            prev_usd = float(bar["sumOpenInterestValue"])

    oi_24h_pct = ""
    if prev_usd:
        oi_24h_pct = round((oi_usd / prev_usd - 1) * 100, 2)

    row = {
        "date": day,
        "oi_usd": round(oi_usd, 2),
        "oi_24h_pct": oi_24h_pct,
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
