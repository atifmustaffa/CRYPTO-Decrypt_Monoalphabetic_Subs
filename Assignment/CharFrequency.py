"""
Cyptography
Count frequency of char
"""
import os

print("Analyse character frequency")
file_name = input("Enter filename(same directory): ")
if not os.path.exists(file_name):
	print("File '" + file_name + "' is not exists")
else:
	file = open(file_name, "r")
	text = file.read()
	text = text.replace(" ", "").replace("\n", "") #Remove newlines and spaces
	text = text.lower(); #Convert text to lowercase

	char_arr = []
	char_count_arr = []

	count = 0
	while(len(text) > 0):
	  current_char = text[0];
	  char_arr.append(current_char)
	  char_count_arr.append(text.count(current_char))
	  text = text.replace(current_char, "") #Remove char from text
	  count += 1

	print("CHARACTER FREQUENCY")
	for x in range(0, len(char_arr)):
		print(char_arr[x], char_count_arr[x])
input()
