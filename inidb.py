#! /usr/bin/python
#
import sqlite3

fdb = '/home/pi/print.db'

def createtables():
  conn = sqlite3.connect(fdb)
  c = conn.cursor()

  c.execute("CREATE TABLE IF NOT EXISTS printlog(timestamp DATE DEFAULT (datetime('now','localtime')), comment text, err INTEGER default 0)")
  c.execute("CREATE TABLE IF NOT EXISTS printid(id Integer primary key, barcode text, timestamp DATE DEFAULT (datetime('now','localtime')))")

  c.execute('SELECT * FROM printid')
  print c.fetchall()

  c.execute('SELECT * FROM printlog')
  print c.fetchall()

  #c.execute("DELETE FROM printlog")
  #c.execute("DELETE FROM printid")
  #c.execute("DROP TABLE printid")

  conn.commit()

  conn.close()


if __name__ == "__main__":
  createtables()

