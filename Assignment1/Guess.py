"""
Atif Mustaffa
Cyptography
Guess the key
"""
import os
import random
from EncDec import decrypt

def new_guess(old_key, char_guess):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	char_guess = char_guess.split("=")
	ch1 = char_guess[0]
	ch2 = char_guess[1]
	new_key = old_key.replace(ch1, "!").replace(ch2, ch1).replace("!", ch2)
	return new_key

print("Guess monoalphabetic key")
file_name = input("Enter TEXT filename(same directory): ")
if not os.path.exists(file_name):
	print("File '" + file_name + "' is not exists")
else:
	file = open(file_name, "r")
	text = file.read()
	guess_file_name = input("Enter GUESS filename(same directory): ")
	if not os.path.exists(guess_file_name):
		print("File '" + guess_file_name + "' is not exists")
	else:
		guess_file = open(guess_file_name, "r")
		guess = guess_file.read().split("\n")
		alphabets = "abcdefghijklmnopqrstuvwxyz"

		count = 0;
		while count < len(guess):
			print("\nGuess", count+1, ":", guess[count])
			print("Text :", decrypt(text, guess[count]))
			count += 1
		char_guess = input("\nKey = " + guess[count-1] + "\nAlp = " + alphabets + "\nCharacter to swap (Example: e=a) **0 to stop swapping**: ")
		while char_guess != "0":
			new_key = new_guess(guess[count-1], char_guess)
			print("\nGuess", count+1, ":", new_key)
			print("Text :", decrypt(text, new_key))
			guess.append(new_key)
			count += 1
			guess_file = open(guess_file_name, "a")
			guess_file.write("\n"+new_key)
			guess_file.close()
			char_guess = input("\nKey = " + new_key + "\nAlp = " + alphabets + "\nCharacter to swap (Example: e=a) **0 to stop swapping**: ")

input()