import time
import csv
from datetime import datetime
import webbrowser as we

print("Hey there! I am your Zoom Assistant!\n")
time.sleep(1)
print("I will give you alerts for your upcoming Zoom meetings.")
print("I will also help you to find your meetings ID and password.\n\n")
time.sleep(1.5)


def time_diff(a,b):
	list_a = [int(x) for x in a.split(":")]
	list_b = [int(x) for x in b.split(":")]

	value_a = list_a[0]*60 + list_a[1]
	value_b = list_b[0]*60 + list_b[1]

	ans = value_a - value_b
	return ans


def search(timestr):
	query = []
	with open("meetings.csv", "r") as rfile:
		my_reader = csv.reader(rfile)
		next(my_reader)
		for line in my_reader:
			csv_time = line[0].split(",")
			if not len(line) == 0:
				difference = time_diff(timestr[1],csv_time[1])
				if timestr[0]==csv_time[0] and abs(difference) <= 5:
					expected_line = line
					expected_line.append(difference)
					query.append(expected_line)
	return query

while True:
	print("Searching for Zoom Meetings....\n")
	time.sleep(1.5)
	timestr = (datetime.now().strftime("%a,%H:%M")).split(",")
	query = search(timestr)

	if len(query) == 0:
		print("No meeting found!")

	for line in query:
		print("Meeting Alert!")
		if line[-1] < 0:
			print("Meeting will start in",-(line[-1]),"minutes")
		else:
			print("Meeting started",line[-1],"minutes ago")
		print()
		time.sleep(2)
		link = line[3] if len(line[3])!=0 else "Please enter the link of your own"
		print("Meeting Info : ",line[4])
		print("Meeting ID   : ",line[1])
		print("Meeting Pass : ",line[2])
		print("Meeting Link : ",link)
		open_web = input("\nDo you want to open the meeting link? (yes/no) ->").split().lower()
		if open_web == "yes":
                        print("\nOpening meeting link")
                        time.sleep(1)
                        we.open(link)
                else:
                        print("\nCopy and Paste Meeting ID and Password.")
		
		time.sleep(2)
	else:
		close = input("\n\nDo you want to close the program?\na. close\nb. Don't close\n(a/b) -> ").lower()
		time.sleep(1)
		if close == "a":
			print("\n\nThanks for taking assist from Zoom Assistant.")
			time.sleep(1)
			print("Creator- Ahammad Shawki 8\n")
			time.sleep(3)
			break

		else:
			print("\nSleeping from 5 minutes")
			time.sleep(60*5)


