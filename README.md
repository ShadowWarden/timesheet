timesheet is a simple timekeeping script written in python. Originally meant as a way for me to keep track of the number of hours I was spending on classes and projects, the script writes information about classes attended (or not) in a logfile ~/.timesheetlog. 

To run the program, simply say 
	
	python timesheet py [options]

or
	
	./timesheet.py [options]

Valid options are as follows:

a : Absent. Use this to enter a class that you missed in the log. You need to give three arguments, the class name, date and a small commit message citing your reason for missing the lecture. For instance

	./timesheet.py a CHY211 31/08/16 "Too many curly arrows"

p: Present. Use this to enter a class that you attended. Takes two arguments, the class name and date.

	./timesheet.py p APPM3010 31/08/16

hw: Homework. Use this to record hours spent working on a particular class. Takes 5 arguments, class name, date, start time, end time and a commit message. Both times have to be given in T%H:%M. For instance

	./timesheet.py hw APPM3010 31/08/16 T20:00 T22:00 "Finished HW 1"

np: Number present. Prints the number of classes attended along with the total classes so far for the class. Takes one argument, namely the class name.

	./timesheet.py np APPM3010

show: Prints the contents of the log file.

	./timesheet.py show

hours: Prints total hours spent on a class. Take one argument in the class name. 
NOTE: hours treats all classes as 1 hour long.

	./timesheet.py hours APPM3010

You must have python 3.0 for the script to run (just change the print statements to the right syntax if you have 2.7)
