import sqlite3
# from IMP import NewWindow
conn = sqlite3.connect('FaceRecognition.db')
c = conn.cursor()

name=c.execute("SELECT * FROM AOD_2020_07_06")
print(name.fetchall())	
conn.commit()
conn.close()
