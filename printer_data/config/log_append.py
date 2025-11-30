#!/usr/bin/env python3
import sys
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("/home/ed/printer_data_logs/klippy.log")

msg = " ".join(sys.argv[1:])  # everything after the script path
ts = datetime.now().isoformat(timespec="seconds")

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
with LOG_PATH.open("a", encoding="utf-8") as f:
    f.write(f"{ts} {msg}\n")

