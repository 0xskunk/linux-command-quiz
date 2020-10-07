#!/bin/python3
import sys
from art import *
from colorama import init
from colorama import Fore, Back, Style
import time


#Make the colours easier to use
red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.CYAN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT

def banner():
	title = "- Quiz Time -"
	header = text2art(title, font='speed')
	print(blue+ header + white + "[*] Test your linux knowledge and get comfortable using the command line! - Toby Jackson (0xskunk)\n")

def line_break():
	print("-" * 40)

def welcome_menu():
	banner()
	line_break()
	print(white + "[*] Ready to get started?")
	response = input(yellow + "[?] Y/N: ")
	line_break()
	response = response.lower()
	if response == "y":
		gametime()
	elif response == "n": 
		print(red + "[!] That's a shame.. Maybe later.")
		sys.exit()
	else:
		print(red + "[!] I didn't understand that response!")
		sys.exit()


def gametime():
	line_break()
	print(white +"[*] So how well do you know your way around the terminal?")
	print(yellow + "[*] Loading list of questions...")
	for i in range (1, 60):
		time.sleep(0.03)
		print(yellow + "#", end="", flush=True)
	print("\n")
	score = 0
	q1 = input(white +"[*] How do you list files in your directory: ")
	q1 = q1.lower()
	if q1 == "ls":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ls'!")
	line_break()

	q2 = input(white +"[*] How do you change directories: ")
	q2 = q2.lower()
	if q2 == "cd":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cd'!")
	line_break()

	q3 = input(white +"[*] What tool is primarily used for scanning a target during enumeration: ")
	q3 = q3.lower()
	if q3 == "nmap":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'nmap'!")
	line_break()

	q4 = input(white +"[*] What file holds information about all the user acccounts that exist on the device: ")
	q4 = q4.lower()
	if "passwd" in q4:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is '/etc/passwd'!")
	line_break()

	q5 = input(white +"[*] How do you return the current user that you are logged in as: ")
	q5 = q5.lower()
	if q5 == "whoami" or q5 == "id":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'whoami' or 'id'!")
	line_break()

	q6 = input(white +"[*] How do you print your current working directory: ")
	q6 = q6.lower()
	if q6 == "pwd":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'pwd'!")
	line_break()

	q7 = input(white +"[*] If you want to perform a command as a super user, you prefix your command with what word: ")
	q7 = q7.lower()
	if q7 == "sudo":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'sudo'!")
	line_break()

	q8 = input(white +"[*] The command used to switch users in the terminal is:  ")
	q8 = q8.lower()
	if q8 == "su":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'su'!")
	line_break()

	q9 = input(white +"[*] How do you view currently running processes: ")
	q9 = q9.lower()
	if "ps" in q9:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ps aux'!")
	line_break()

	q10 = input(white +"[*] What very well known command allows you to search for a word in terminal output: ")
	q10 = q10.lower()
	if "grep" in q10:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'grep'!")
	line_break()

	q11 = input(white +"[*] If you want to make a new directory, you should type: ")
	q11 = q11.lower()
	if q11 == "mkdir":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'mkdir'!")
	line_break()

	q12 = input(white +"[*] How would you remove a file in the terminal: ")
	q12 = q12.lower()
	if q12 == "rm":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'rm'!")
	line_break()

	q13 = input(white + "[*] If a file has readable text, how do you print the contents to the terminal (Meow): ")
	q13 = q13.lower()
	if q13 == "cat":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cat'!")
	line_break()

	q14 = input(white +"[*] I need to move a file, what do I type: ")
	q14 = q14.lower()
	if q14 == "mv":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'mv'!")
	line_break()

	q15 = input(white +"[*] How do I copy a file: ")
	q15 = q15.lower()
	if q15 == "cp":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'cp'!")
	line_break()


	q16 = input(white +"[*] What about getting the wordcount of a file: ")
	q16 = q16.lower()
	if "wc" in q16:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'wc'!")
	line_break()


	q17 = input(white +"[*] How would I append a line to the bottom of my text file: ")
	q17 = q17.lower()
	if  ">>" in q17:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is with >>. For example 'echo hello world >> file.txt' appends hello world to the bottom of file.txt")
	line_break()


	q18 = input(white +"[*] Which command will print what type of file a file is (According to the data they contain): ")
	q18 = q18.lower()
	if q18 == "file":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'file'!")
	line_break()

	q19 = input(white +"[*] How do I add a user: ")
	q19 = q19.lower()
	if "adduser" in q19:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'adduser'!")
	line_break()

	q20 = input(white +"[*] And then, how could one delete that user: ")
	q20 = q20.lower()
	if q20 == "deluser":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'deluser'!")
	line_break()

	q21 = input(white +"[*] How do you edit file permissions: ")
	q21 = q21.lower()
	if q21 == "chmod":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'chmod'!")
	line_break()

	q22 = input(white +"[*] What command changes file or directory ownership: ")
	q22 = q22.lower()
	if q22 == "chown":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'chown'!")
	line_break()

	q23 = input(white +"[*] How do you list hidden files that start with a period (.ssh for example): ")
	q23 = q23.lower()
	if "-a" in q23 or "-la" in q23:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ls -a'!")
	line_break()

	q24 = input(white +"[*] What is the super-user account called in linux: ")
	q24 = q24.lower()
	if q24 == "root":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'root'!")
	line_break()

	q25 = input(white +"[*] What command creates an empty file: ")
	q25 = q25.lower()
	if q25 == "touch":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'touch'!")
	line_break()

	q26 = input(white +"[*] How would I print the first 10 lines of a file: ")
	q26 = q26.lower()
	if q26 == "head":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'head'!")
	line_break()

	q27 = input(white +"[*] What about the last 10 lines: ")
	q27 = q27.lower()
	if q27 == "tail":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'tail'!")
	line_break()

	q28 = input(white +"[*] How do I print system/kernel information: ")
	q28 = q28.lower()
	if "uname" in q28:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'uname -a'!")
	line_break()

	q29 = input(white +"[*] How do you view your IP address: ")
	q29 = q29.lower()
	if "ifconfig" in q29 or "ip addr" in q29:
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ifconfig' or 'ip addr'!")
	line_break()

	q30 = input(white +"[*] How would you try to login via ssh to the account 'david' on 192.168.137.69: ")
	q30 = q30.lower()
	if q30 == "ssh david@192.168.137.69":
		print("[*]" + green + " CORRECT!")
		score += 1
	else:
		print("[!]" + red + " WRONG! The answer is 'ssh david@192.168.137.69'!")
	line_break()
	
	if score == 30:
		print(green + "[*] Unbelievable! You scored: " + str(score) + ". Ride oooooooooooon! ;)")
		line_break()

	elif score >= 25 and score < 30:
		print(green + "[*] Congratulations, you scored: " + str(score) + ". Cracking result! :)")
		line_break()

	elif score >= 15 and score < 25:
		print(yellow + "[*] Nice, you scored: " + str(score) + ". Not bad at all! :)")
		line_break()

	elif score >= 5 and score < 15: 
		print(yellow + "[?] Definitely room for improvement. You scored " + str(score) + " :/")
		line_break()

	else:
		print(red + "[!] Going to need to work on that I think. You scored " + str(score) + " :(")
		line_break()

def close_program():
	while True:
		print(white + "[*] Would you like to try again?")
		quit = input(yellow + "[*] Yes or No: ")
		quit = quit.lower()	
		if quit == "yes":
			welcome_menu()
	
		elif quit == "no":
			footer()
			sys.exit()
	
		else:
			print("[*]" + red + " That's not a yes or no...")
			line_break()
			
def footer():
	title = "skunk"
	header = text2art(title, font='speed')
	print(blue + header + "[*] Hope you learnt something <3 \n")



init(autoreset=True)

try:
	welcome_menu()
	close_program()

except KeyboardInterrupt:
    print(red + "\nYou pressed Ctrl + C to exit!")
    sys.exit()