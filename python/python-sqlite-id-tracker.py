import sqlite3
from datetime import datetime, timezone
from typing import Any, List, Tuple


class SqliteIdTracker:
	"""Simple wrapper for performing SQLite3 operations to check if an ID is in a database or not."""
	def __init__(self, file=None):
		"""Initializes the object.

		Args:
			file: path to an existing or yet-to-be-created database
		"""
		self.connection = None
		self.cursor = None
		self.file = file
		self.table = "IDS"

	def connect(self) -> None:
		"""Connects to the database and creates internal connection and cursor objects."""
		if self.file:
			self.connection = sqlite3.connect(self.file)
			self.cursor = self.connection.cursor()

	def setup(self) -> None:
		"""Creates the main table and creates the column_names list attribute."""
		if self.cursor:
			self.cursor.execute(f"""
				CREATE TABLE IF NOT EXISTS {self.table} (
					id TEXT PRIMARY KEY,
					epoch INTEGER
				)
			""")
			self.connection.commit()
			# set column_names attribute
			self.cursor.execute(f"SELECT * FROM {self.table} LIMIT 0")
			self.column_names = [description[0] for description in self.cursor.description]

	def commit(self) -> None:
		"""Commits database transactions. Available publicly and privately."""
		if self.connection:
			self.connection.commit()

	def select_id(self, id: str) -> Tuple:
		"""Selects and returns a database row by ID value.

		Args:
			id: the primary key to be located, which is an ID generated externally (UUID, _id, etc.)

		Returns:
			the selected row as a tuple; use with the column_names attribute for reference
		"""
		if self.cursor:
			query = (f"SELECT * FROM {self.table} WHERE id=? LIMIT 1")
			# bool
			#return self.cursor.execute(query, (id,)).fetchone() is not None
			# cursor row
			return self.cursor.execute(query, (id,)).fetchone()

	def select_all(self) -> List[Tuple[Any]]:
		"""Selects and returns all database rows.

		Returns:
			all rows as a list of tuples; use with the column_names attribute for reference
		"""
		if self.cursor:
			query = (f"SELECT * FROM {self.table}")
			return self.cursor.execute(query).fetchall()

	def insert_id(self, id: str, commit: bool=False) -> None:
		"""Inserts a new row with a given ID.

		Args:
			id: the primary key to be inserted, which is an ID generated externally (UUID, _id, etc.)
			commit: choose whether to commit after this action
		"""
		if self.cursor:
			now = int(datetime.now(timezone.utc).timestamp())
			query = (f"INSERT OR IGNORE INTO {self.table} (id, epoch) VALUES (?,?)")
			self.cursor.execute(query, (id, now))
			if commit:
				self.connection.commit()

	def refresh_id(self, id: str, commit: bool=False) -> None:
		"""Updates new row with a given ID with the current timestamp as an epoch (seconds).

		Args:
			id: the primary key to be updated, which is an ID generated externally (UUID, _id, etc.)
			commit: choose whether to commit after this action
		"""
		if self.cursor:
			now = int(datetime.now(timezone.utc).timestamp())
			query = (f"UPDATE {self.table} SET epoch=? WHERE id=?")
			self.cursor.execute(query, (now, id,))
			if commit:
				self.connection.commit()

	def delete_id(self, id: str, commit: bool=False) -> None:
		"""Deletes a row with a given ID.

		Args:
			id: the primary key to be deleted, which is an ID generated externally (UUID, _id, etc.)
			commit: choose whether to commit after this action
		"""
		if self.cursor:
			query = (f"DELETE FROM {self.table} WHERE id=?")
			self.cursor.execute(query, (id,))
			if commit:
				self.connection.commit()

	def cleanup(self, days: int=0, hours: int=0, minutes: int=0, seconds: int=0, commit: bool=False) -> None:
		"""Delete all records older than x interval. Priority: seconds (first), minutes, hours, days (last).

		Args:
			days: delete all entries older than this number of days
			hours: delete all entries older than this number of hours
			minutes: delete all entries older than this number of minutes
			seconds: delete all entries older than this number of seconds
			commit: choose whether to commit after this action
		"""
		clean = 0
		if days > 0:
			clean = days * 86400
		if hours > 0:
			clean = hours * 3600
		if minutes > 0:
			clean = minutes * 60
		if seconds > 0:
			clean = seconds
		if self.cursor:
			if clean > 0:
				now = int(datetime.now(timezone.utc).timestamp())
				keep_newer_than_this = now - clean
				query = (f"DELETE FROM {self.table} WHERE epoch < ?")
				self.cursor.execute(query, (keep_newer_than_this,))
				if commit:
					self.connection.commit()

	def close(self, commit: bool=False):
		"""Closes the database connection.

		Args:
			commit: choose whether to commit after this action
		"""
		if self.connection:
			if commit:
				self.connection.commit()
			if self.connection:
				self.connection.close()


if __name__ == "__main__":
	#
	import time
	#
	ids = [
		"ba16fc4c-d60d-466d-93e8-671375c9bede",
		"fb461637-8437-49d7-9e2a-c2c6cb00e6ae",
		"5b3d04a1-5de8-4301-a1eb-5b6c72228162",
		"e5d8fbae-09d0-46a4-93b5-e9f034d87a11",
		"9d3a55a9-faf1-4744-8c2a-ae925231f1b8",
	]
	#
	print("\ncreate object")
	s = SqliteIdTracker(file="registry.sqlite")
	#
	print("\nconnect")
	s.connect()
	#
	print("\nsetup")
	s.setup()
	#
	print("\ncolumn_names")
	print(s.column_names)
	#
	print("\ninsert_id - runs twice to test INSERT OR IGNORE")
	for id in ids:
		s.insert_id(id, commit=True)
		s.insert_id(id, commit=True)
	#
	print("\nselect_id - runs twice to get the first two IDs")
	print("RECORD 1:", s.select_id(ids[0]))
	print("RECORD 2:", s.select_id(ids[1]))
	#
	print("\nselect_all - should return tuples of IDs and epochs")
	rows = s.select_all()
	print(f"type {type(rows).__name__}, length {len(rows)}:")
	for r in rows:
		print(type(r), r)
	#
	print("\nrefresh_id - sleeping for 1 second")
	time.sleep(1)
	s.refresh_id(ids[0], commit=True)
	print("refreshed record 1 with a new epoch:", s.select_id(ids[0]))
	#
	print("\ndelete_id")
	s.delete_id(ids[0], commit=True)
	print(f"DELETED {ids[0]} (select_id should return None):", s.select_id(ids[0]))
	#
	print("\ncleanup - delete all records older than 2 seconds (should return an empty list)")
	time.sleep(2)
	s.cleanup(seconds=1, commit=True)
	print(s.select_all())
	s.close()


# expected output
'''
$ uv run sqlite-id-tracker.py

create object

connect

setup

column_names
['id', 'epoch']

insert_id - runs twice to test INSERT OR IGNORE

select_id - runs twice to get the first two IDs
RECORD 1: ('ba16fc4c-d60d-466d-93e8-671375c9bede', 1773800768)
RECORD 2: ('fb461637-8437-49d7-9e2a-c2c6cb00e6ae', 1773800768)

select_all - should return tuples of IDs and epochs
type list, length 5:
<class 'tuple'> ('ba16fc4c-d60d-466d-93e8-671375c9bede', 1773800768)
<class 'tuple'> ('fb461637-8437-49d7-9e2a-c2c6cb00e6ae', 1773800768)
<class 'tuple'> ('5b3d04a1-5de8-4301-a1eb-5b6c72228162', 1773800768)
<class 'tuple'> ('e5d8fbae-09d0-46a4-93b5-e9f034d87a11', 1773800768)
<class 'tuple'> ('9d3a55a9-faf1-4744-8c2a-ae925231f1b8', 1773800768)

refresh_id - sleeping for 1 second
refreshed record 1 with a new epoch: ('ba16fc4c-d60d-466d-93e8-671375c9bede', 1773800769)

delete_id
DELETED ba16fc4c-d60d-466d-93e8-671375c9bede (select_id should return None): None

cleanup - delete all records older than 2 seconds (should return an empty list)
[]
'''
