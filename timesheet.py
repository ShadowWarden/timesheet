# timesheet.py
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#
# Time keeping python script for coursework.
#

__author__ = "Omkar H. Ramachandran <omkar.ramachandran@gmail.com>"
__date__ = '28/08/2017'

import sys
import subprocess
import os.path
from datetime import datetime

path = "/home/omkar/.timesheetlog"

if(os.path.isfile(path) == False):
	vprocess = subprocess.call(["touch","/home/omkar/.timesheetlog"])
	print(".timesheet not found. Creating log file")
	
ins = open("/home/omkar/.timesheetlog","a+")

if(sys.argv[1] == 'a'):
	if(len(sys.argv) != 5):
		print("If 'a', then 3 arguments (Class Name, Date and reason for absence) have to be given")
		sys.exit(1)
	else:
		data = ["A",sys.argv[2],sys.argv[3],sys.argv[4]]
elif(sys.argv[1] == 'p'):
	if(len(sys.argv) != 4):
		print("If 'p' then 2 arguments (Class Name and Date) have to be given")
		sys.exit(1)
	else:
		data = ["P",sys.argv[2],sys.argv[3]]
elif(sys.argv[1] == 'hw'):
	if(len(sys.argv) != 7):
		print("If 'HW' then 5 arguments (Class Name, Date, Start Time, End Time, Commit Note) have to be given")
		sys.exit(1)
	else:
		print("Start time:",sys.argv[4])
		print("End Time:",sys.argv[5])
		data = ["HW",sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]]
elif(sys.argv[1] == "np"):
	if(len(sys.argv) != 3):
		print("If NP then need class number")
		sys.exit(1)
	
	Fin = open(path,"r")
	data = []
	lines = [line.rstrip() for line in Fin.readlines()]
	for line in lines:
		number_strings = line.split('|')
		data.append(number_strings)
	num_present = 0
	total = 0	
	for i in range(len(data)):
		if(data[i][1] == sys.argv[2]):
			if(data[i][0] == 'P'):
				total += 1 
				num_present += 1
			elif(data[i][0] == 'A'):
				total += 1
	print("Recorded Attendence for",sys.argv[2])
	print("Number present =",num_present)
	print("Total Classes so far =",total)
	print("Percent present =",float(num_present)/total*100)
	sys.exit(0)
elif(sys.argv[1] == 'hours'):
	if(len(sys.argv) != 3):
		print("If hours, then need class name")
	Fin = open(path,"r")
	data = []
	lines = [line.rstrip() for line in Fin.readlines()]
	for line in lines:
		number_strings = line.split('|')
		data.append(number_strings)
	total = 0	
	for i in range(len(data)):
		if(data[i][1] == sys.argv[2]):
			if(data[i][0] == 'P'):
				total += 1 
			if(data[i][0] == 'HW'):
				d1 = datetime.strptime(data[i][3], "T%H:%M")
				d2 = datetime.strptime(data[i][4], "T%H:%M")
				total += (d2-d1).total_seconds()/60.0/60.0
	print("Recorded Hours spent for",sys.argv[2])
	print("Total Hours spent on homeworks and class so far =",total)
	sys.exit(0)

elif(sys.argv[1] == 'show'):
	subprocess.call(["less",path])
	sys.exit(1)

for i in data:
	ins.write("%s|" % i)

ins.write("\n")
