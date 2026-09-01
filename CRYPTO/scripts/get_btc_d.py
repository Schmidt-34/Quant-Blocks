#!/usr/bin/env python3
"""Pull today's BTC.D from CoinGecko. Append-only to onchain/btc_d.csv."""

import csv
import json
import ssl
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
OUT = ROOT / "onchain" / "btc_d.csv"
URL = "https://api.coingecko.com/api/v3/global"
SOURCE = "coingecko.com/api/v3/global"
FIELDS = ["date", "value", "unit", "source"]


def main() -> None:
    req = urllib.request.Request(URL, headers={"User-Agent": "Quant-Blocks-CRYPTO/0.1"})
    with urllib.request.urlopen(req, timeout=20, context=https_context()) as resp:
        data = json.load(resp)["data"]

    day = datetime.fromtimestamp(data["updated_at"], tz=timezone.utc).date().isoformat()
    row = {
        "date": day,
        "value": round(float(data["market_cap_percentage"]["btc"]), 4),
        "unit": "percent",
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
