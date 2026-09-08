#!/usr/bin/env python3
"""Pull today's Binance BTCUSDT spot taker buy/sell. Cumulate CVD.

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
OUT = ROOT / "trading" / "cvd_spot.csv"
KLINE_URL = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=2"
SOURCE = "api.binance.com BTCUSDT spot"
FIELDS = [
    "date",
    "buy_vol",
    "sell_vol",
    "delta",
    "cvd",
    "z",
    "source",
]
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


def last_cvd() -> float:
    if not OUT.exists():
        return 0.0
    with OUT.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0.0
    return float(rows[-1]["cvd"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--z", help="Optional. Z from the chart.")
    args = parser.parse_args()

    qmi = qmi_today()
    z = args.z if args.z else f"{float(qmi['Z_Score']):.2f}"
    print(f"QMI {qmi.get('Date', '')}  Z={z}")

    bars = get(KLINE_URL)
    today = datetime.now(timezone.utc).date().isoformat()
    chosen = None
    day = None
    for bar in bars:
        bar_day = datetime.fromtimestamp(int(bar[0]) / 1000, tz=timezone.utc).date().isoformat()
        if bar_day == today:
            chosen = bar
            day = bar_day
    if chosen is None:
        sys.exit(f"no 1d kline for {today}")

    vol = float(chosen[5])
    buy_vol = float(chosen[9])
    sell_vol = vol - buy_vol
    delta = buy_vol - sell_vol
    cvd = last_cvd() + delta

    row = {
        "date": day,
        "buy_vol": round(buy_vol, 4),
        "sell_vol": round(sell_vol, 4),
        "delta": round(delta, 4),
        "cvd": round(cvd, 4),
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
