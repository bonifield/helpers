#!/usr/bin/env python3

from datetime import datetime

u = datetime.utcnow()

epoch = u.timestamp()
iso8601 = u.isoformat(sep="T", timespec="auto")

print(f"Current UTC Epoch: {epoch}\tISO8601: {iso8601}")
