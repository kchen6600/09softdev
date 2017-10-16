import csv
import sqlite3

data = "peepscourses.db"

db = sqlite3.connect(data)
c = db.cursor()

command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)" #put SQL statement in this string
command2 = "CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)"

c.execute(command) #run SQL statement
c.execute(command2)


with open("data/courses.csv") as csvfile:
	read = csv.DictReader(csvfile)
	for row in read:
		courseinfo = "'" + row["code"]+ "', '" +row["mark"]+ "', '" +row["id"]+"'"
		add_course = "INSERT INTO courses VALUES("+courseinfo+")"
		c.execute(add_course)

with open("data/peeps.csv") as csvfile:
	read = csv.DictReader(csvfile)
	for row in read:
		courseinfo = "'"+row["name"]+ "', '" +row["age"]+ "', '" +row["id"]+"'"
		add_peep = "INSERT INTO peeps VALUES ("+courseinfo+")"
		c.execute(add_peep)
	
db.commit() #save changes
db.close() #close database

