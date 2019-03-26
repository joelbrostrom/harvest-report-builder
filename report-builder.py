import math
import re
import os

previous_durations =[]
duration_sum = 0
commit_message = ""

def calculate_difference(time):
	short_dash = '\xe2\x80\x93'
	startInMinutes = 0
	endInMinutes = 0
	startEndPair = map(lambda s : s.strip(), re.split('-|' + short_dash, time))

	if len(startEndPair) == 1:
		endInMinutes = string_to_minutes(startEndPair[0])
	elif len(startEndPair) == 2:
		startInMinutes = string_to_minutes(startEndPair[0])
		endInMinutes = string_to_minutes(startEndPair[1])
	else:
		pass

	duration = endInMinutes - startInMinutes

	durationString = min_to_string(duration)

	return duration

def string_to_minutes(str):
	hourMinutesSplit = str.split(":")
	if len(hourMinutesSplit) == 1:
		minutes = int(hourMinutesSplit[0])
	elif len(hourMinutesSplit) == 2:
		minutes = int(hourMinutesSplit[0]) * 60 + int(hourMinutesSplit[1])
	else:
		minutes = 0

	return minutes

def min_to_string(duration):
		return "%d:%02d" % (math.floor((duration/60)), duration%60)

def print_result():
	os.system("clear")
	print("\n")
	for dur_str in previous_durations:
		print(dur_str)
	 	
	print("-----------------\ntotal:      = " + min_to_string(duration_sum) + "\n")

	if len(commit_message) > 0:
		print(commit_message + "\n")

while True:
	input_text = raw_input("Time: ")
	try:
		if (input_text == 'n') or (input_text == "new"):
			os.system("clear")
			print("_____New Calculation_____\n")
			previous_durations = []
			duration_sum = 0
		elif input_text == "l":
			input_int = raw_input("lunch in minutes: ")
			duration_sum -= int(input_int)
			previous_durations.append("lunch:      - " + min_to_string(int(input_int)))
			print_result()
		elif input_text == "m":
			done = False
			print("type \"done\" to save and exit\nmessage:")
			while not done:
				new_line = raw_input(">")
				if new_line == "done":
					done = True
				else:
					commit_message += new_line + "\n"
			print_result()
		elif input_text == "s":
			print_result()
		elif (input_text == 'q') or (input_text == "e"):
			print("closing application")
			break
		else:
			new_duration = calculate_difference(input_text)
			duration_sum += new_duration
			previous_durations.append(input_text + ' = ' + min_to_string(new_duration))
			print_result()
	except:
		print("\nInvalid input.\nDid you mean:\nn => Start new day\nl => Add lunch break\nm => Add message to output\ns => Show current report\nq or e => Quit/Exit app\n")

