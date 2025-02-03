#!/usr/bin/env python3

from datetime import datetime, timezone

u = datetime.now(timezone.utc)

epoch = u.timestamp()
human = u.strftime("%Y-%m-%d %H:%M:%S") #.%f")
iso8601 = u.isoformat(sep="T", timespec="auto")
tools = u.strftime("%Y%m%d%H%M%S")

print(f"Current UTC Epoch: {epoch}\tISO8601: {iso8601}\tHuman: {human}\tTools: {tools}")
