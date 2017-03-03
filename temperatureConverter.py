#02 temperature converter

allow = False
#wybór kierunku konwersji
while not allow:
	choose = input('''Wybierz kierunek konwersji:
	C -> F (1)
	C -> K (2)
	F -> C (3)
	F -> K (4)
	K -> C (5)
	K -> F (6)\n''')
	allow = str(choose).isdigit()
	if (allow == True):
		if (int(choose) > 0) and (int(choose) < 7):
			pass
		else:
			allow = False						
choose = int(choose)
			
type = (('C','F'),('C','K'),('F','C'),('F','K'),('K','C'),('K','F'))	
skala1 = type[choose-1][0]
skala2 = type[choose-1][1]


#wybór temperatury
allow = False
while not allow:
	tempIn = input('Podaj temperaturę wejsciową: ')
	allow = str(tempIn).isdigit()
	if (tempIn == ''):
		pass
	else:
		#liczba ujemna
		if (str(tempIn)[0] == '-'):
			if (str(tempIn)[1:].isdigit()):
				allow = True
			#liczba ujemna dziesiętna	
			elif str(int(float(str(tempIn)[1:]))).isdigit():
				allow = True
	#liczba dziesiętna			
	try:
		allow2 = str(int(float(tempIn))).isdigit()
		if allow2:
			allow = True
		#wykorzystujemy w poniższej funkcji
		tempIn = float(tempIn)
	except:
		tempIn = 0
		pass
	
	#sprawdzenie, czy podana temperatura miesci się w skali
	if allow:	
		if ((choose == 1) or (choose == 2)) and tempIn < -273.15: allow = False
		elif ((choose == 3) or (choose == 4)) and tempIn < -459.67: allow = False
		elif ((choose == 5) or (choose == 6)) and tempIn < 0: allow = False
		if not (allow):
			print('Temperatura poza skalą')
	

tempOut	= 0 
if (choose == 1):
	tempOut = tempIn*(9/5) + 32
elif (choose == 2):
	tempOut = tempIn + 273.15
elif (choose == 3):
	tempOut = (tempIn-32)*(5/9)
elif (choose == 4):
	tempOut = (tempIn-32)*(5/9) + 273.15
elif (choose == 5):
	tempOut = tempIn - 273.15
elif (choose == 6):
	tempOut = (tempIn-273.15)*(9/5) + 32
else:
	print('wrong choice')

print('Oto wynik:')
print(tempIn, skala1,'=', tempOut, skala2)
 