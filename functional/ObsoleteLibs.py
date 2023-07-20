# Pathlib 而不是 OS
from pathlib import Path
import os.path

# 老方式
two_dirs_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 新方式，可读性强
two_dirs_up = Path(__file__).resolve().parent.parent
readme = Path("README.md").resolve()
print(f"Absolute path: {readme.absolute()}")
# Absolute path: /home/martin/some/path/README.md
print(f"File name: {readme.name}")
# File name: README.md
print(f"Path root: {readme.root}")
# Path root: /
print(f"Parent directory: {readme.parent}")
# Parent directory: /home/martin/some/path
print(f"File extension: {readme.suffix}")
# File extension: .md
print(f"Is it absolute: {readme.is_absolute()}")
# Is it absolute: True

# Secrets 而不是 OS
# 老方式:
import os

length = 64

value = os.urandom(length)
print(f"Bytes: {value}")
# Bytes: b'\xfa\xf3...\xf2\x1b\xf5\xb6'
print(f"Hex: {value.hex()}")
# Hex: faf3cc656370e31a938e7...33d9b023c3c24f1bf5

# 新方式:
import secrets

value = secrets.token_bytes(length)
print(f"Bytes: {value}")
# Bytes: b'U\xe9n\x87...\x85>\x04j:\xb0'
value = secrets.token_hex(length)
print(f"Hex: {value}")
# Hex: fb5dd85e7d73f7a08b8e3...4fd9f95beb08d77391

# Zoneinfo 而不是 pytz
from datetime import datetime
import pytz  # pip install pytz

dt = datetime(2022, 6, 4)
nyc = pytz.timezone("America/New_York")

localized = nyc.localize(dt)
print(f"Datetime: {localized}, Timezone: {localized.tzname()}, TZ Info: {localized.tzinfo}")

# 新方式:
from zoneinfo import ZoneInfo

nyc = ZoneInfo("America/New_York")
localized = datetime(2022, 6, 4, tzinfo=nyc)
print(f"Datetime: {localized}, Timezone: {localized.tzname()}, TZ Info: {localized.tzinfo}")
# Datetime: 2022-06-04 00:00:00-04:00, Timezone: EDT, TZ Info: America/New_York

# Proper Logging 而不是 print
import logging
logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logging.error("Some serious error occurred.")
# [12:52:35] {<stdin>:1} ERROR - Some serious error occurred.
logging.warning('Some warning.')
# [12:52:35] {<stdin>:1} WARNING - Some warning.
