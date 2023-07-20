import sqlite3
import threading
import time
import Sensors.TemperatureSensor


def initialize():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()
    # 遍历每个数据表名
    for table in tables:
        table_name = table[0]
        cur.execute(f"DELETE FROM {table_name}")
        cur.execute(f"DROP TABLE {table_name}")
    cur.execute("CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY, time TEXT, value REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS humidity (id INTEGER PRIMARY KEY, time TEXT, value REAL)")
    con.commit()
    cur.close()
    con.close()


def dataManage(tempSensor: Sensors.TemperatureSensor.TemperatureSensor):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    temp = tempSensor.get_value()[0]
    humidity = tempSensor.get_value()[1]
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO temperature (time, value) VALUES (?, ?)", (now, temp))
    cur.execute("INSERT INTO humidity (time, value) VALUES (?, ?)", (now, humidity))
    # 提交更改
    con.commit()
    dataManageThread = threading.Timer(240, dataManage, (tempSensor,))
    dataManageThread.start()