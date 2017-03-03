# 10 password generator
import random
'''
lenght -dlugosc hasla
a - obecnosc malych liter
A - obecnosc duzych liter
n - obecnosc cyfr
s - obecnosc znakow specjalnych
'''

def passGenerator(lenght=6, a=True, A=True, n=True, s=True):
	container = ""
	alphabet = "abcdefghijklmnopqrstuwxyz"
	alphabetBig = alphabet.upper()
	numbers = "0123456789"
	specialSigns = '''!@#$%^&*(){}[]\|:";'<>?,./'''
	if (a == True): container += alphabet
	if (A == True): container += alphabetBig
	if (n == True): container += numbers
	if (s == True): container += specialSigns
	password = ""
	for x in range(lenght):
		#wybór pojemnika
		choose = random.randrange(len(container))
		password += container[choose]
	return print('Hasło to: ', password), password
	
def generate():	
	L = []
	for x in range(200):
		#ustawiamy opcje wyboru
		password = passGenerator(12, s=False)[1]
		L.append(password)
	L.sort()
	return L

def writeDictionary(passList):
	#set some real path
	file = open("D:\programming\path\dictionary01.txt", 'w')
	for x in range(len(L)):
		file.write(str(L[x]))
		file.write('\n')
	file.close()

#część wykonawcza		
L = generate()
writeDictionary(L)	
	
	
	