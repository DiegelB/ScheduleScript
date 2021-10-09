#!/usr/bin/python3

import cgi
from main import main

def loadSchedule():
	schedule = []
	with open('schedule.txt') as f:
		for x in f.readlines():
			schedule.append(x)
	return schedule

def changeSchedule(day, task):
	schedule = loadSchedule()
	n = 0
	for x in schedule:
		n+=1
		if x == day + "\n":
			schedule[n] = task
	with open('schedule.txt','w') as f:
		for x in schedule:
			f.writelines(x)

print("Content-type: text/html\n\n")
print("<html><body>")
print("<br><br><br>")

print("<p style='text-align:center'>")
print("<b><h1>")
print("<font color=darkgreen>")
main()
print("</font>")
print("</b></h1>")
print("</p>")
print("<br>")

print("<h3>")
print("<form method='post' action='source.py'>")
print("<p>Day you would like to change: <input type:'text' name='day'/></p>")

print("<p><h5>Task you want to do: <input type:'text' name='task'/></h5></p>")

print("<input type='submit' name='submit' value='Submit'/>")
print("</h3>")
print("</form>")
print("<br><br>")

form = cgi.FieldStorage()

if form.getvalue("day"):
	day = form.getvalue("day")
if form.getvalue("task"):
	task = form.getvalue("task")
	changeSchedule(day, task)


print("</body></html>")

