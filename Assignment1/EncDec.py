"""
Atif Mustaffa
Cyptography
Encrypt or Decrypt text
"""
import os

def decrypt(ciphertext, key):
	plaintext = ""
	for i in range(0, len(ciphertext)):
		plaintext += swap_letter(ciphertext[i], key, "de")
	return plaintext

def encrypt(plaintext, key):
	ciphertext = ""
	for i in range(0, len(plaintext)):
		ciphertext += swap_letter(plaintext[i], key, "en")
	return ciphertext

def swap_letter(ch, key, type):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	if type == "en":
		alphabets, key = key, alphabets

	for i in range(0, len(key)):
		if ch == key[i]:
			return alphabets[i]
	return ch

def main():
	print("Encrypt or decrypt monoalphabetic substitution method")
	file_name = input("Enter TEXT filename(same directory): ")
	if not os.path.exists(file_name):
		print("File '" + file_name + "' is not exists")
	else:
		file = open(file_name, "r")
		text = file.read()

		key_file_name = input("Enter KEY filename(same directory): ")
		if not os.path.exists(key_file_name):
			print("File '" + key_file_name + "' is not exists")
		else:
			key_file = open(key_file_name, "r")
			key = key_file.read()
			
			print("\nText:\n" + text + "\n")
			option = input("\nSelect option:\n1 - Encrypt\n2 - Decrypt\n")
			if option == "1":
				print("\nCiphertext:\n"+encrypt(text, key))
			else:
				print("\nPlaintext:\n"+decrypt(text, key))
# input()