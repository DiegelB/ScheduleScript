from datetime import date
import calendar

#grabs the current day and converts it into readable weekday
def getDay():
	dayName = calendar.day_name[date.today().weekday()]
	return dayName

#loads the schedule.txt file into a list 
def loadSchedule():
	schedule = []
	with open('schedule.txt') as f:
		for x in f.readlines():
			schedule.append(x)
	return schedule

#compares the current day to the day in the text file and
#then returns the corresponding task below the weekday
def getTask():
	schedule = loadSchedule()
	currentDay = getDay()
	n = 0
	for x in schedule:
		n+=1
		if x == currentDay + "\n":
			return schedule[n]
 
#calls all the functions needed and prints out the day
#and the task that needs to be done
def main():
	taskToDo = getTask()
	print("Today is " + getDay() + " you have to "
		  + taskToDo)

	
	
