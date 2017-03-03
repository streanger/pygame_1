#03 calculating age
import time, sys

def checkData():
	dateOfBirth = input('Podaj datę urodzin:\n RRRR,MM,DD np.: 1999,06,30 \n')
	#pobranie daty
	try:
		dateOfBirth = tuple([int(x) for x in dateOfBirth.split(',')])
	#obsługa wyjątku	
	except ValueError:
		print('Błędny zapis. Kończenie...')
		time.sleep(1)
		
	actualDate = time.localtime()[:3]
	#lata przestepne
	leapYears = []
	leap = 2000
	for x in range(20):
		leapYears.append(leap)
		leap -= 4
	leap = 2000
	for x in range(20):
			leap += 4
			leapYears.append(leap)
	leapYears.sort()
	return dateOfBirth, actualDate, leapYears

def ageCalculating(dateOfBirth, actualDate, leapYears):	
	if (dateOfBirth == actualDate):
		return print("You've came here. What a fantastic day!")
	#liczba dni w poszczegónych miesiącach
	daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
	# aY, aM, aD
	# bY, bM, bD
	aY = actualDate[0]
	aM = actualDate[1]
	aD = actualDate[2]
	bY = dateOfBirth[0]
	bM = dateOfBirth[1]
	bD = dateOfBirth[2]	
	#lata, dni, miesiace
	years = 0
	months = 0
	days = 0
	#dni przed urodzeniem, do poczatku roku
	#dni do konca roku, liczac od daty dzisiejszej
	daysBefore = 0
	daysAfter = 0
	daysBetween = 0
	
	#sprawdzenie poprawnosci daty
	if (bY > aY) or (bM > 12) or (bY <= 0) or (bM <=0) or (bD <=0):
		return print('Niepoprawna data')		
	#wykluczenie blednej liczby dni w miesiacu
	if (bM == 2) and (bY in leapYears) and (bD > 29):
		return print('Niepoprawna data; ten miesiac nie ma tylu dni')
	elif bD > daysInMonth[bM-1]:
		return print('Niepoprawna data; ten miesiac nie ma tylu dni')
	#liczba pełnych lat, bez uwzględnienia dni przestepnych
	if (aM > bM): years = aY-bY
	elif (aM < bM): years = aY-bY -1
	else:
		if (aD > bD): years = aY-bY
		elif (aD < bD): years = aY -bY -1
		elif (aD == bD):
			years = aY - bY; months = 0; days = 0;
			return print("Happy birthday! You've got: %s years" % years)	
		
	#dni przed urodzeniem
	for x in range(bM-1):
		daysBefore += daysInMonth[x]
	daysBefore += bD
			
	for x in range(12-aM):
		daysAfter += daysInMonth[11-x]
	daysAfter += daysInMonth[aM-1] - aD	
	
	#dni które minęły od ostatnich urodzin
	if (bM < aM):
		daysBetween = 365 - (daysBefore + daysAfter)
	elif (bM > aM):
		daysBetween = 730 - (daysBefore + daysAfter)
	elif (bM == aM):
		if (bD < aD):
			daysBetween = 365 - (daysBefore + daysAfter)
		elif (bD > aD):
			daysBetween = 730 - (daysBefore + daysAfter)
		elif (bD == aD):
			years = aY - bY; months = 0; days = 0;
			return print("Happy birthday! You've got: %s years" % years)	
	#pełne lata i dni
	fullYandD = (years, daysBetween)
		
	#uwzględnienie lat przestępnych
	#NLY - NumberLeapYears
	yearStart = 0
	yearEnd = 0
	NLY = []
	if (bM > 2):
		yearStart = bY+1
	elif (bM < 3):
		yearStart = bY
		
	#the same for yearEnd
	if (aM > 2):
		yearEnd = aY
	elif (aM < 3):
		yearEnd = aY-1
	
	for x in leapYears:
		if (x >= yearStart) and (x <= yearEnd):
			NLY.append(x)
	NLY = len(NLY)		
	#aftet that count leanYears
	
	#liczba dni ogółem, z uwzględnieniem dni przestępnych
	fullDays = years*365 + daysBetween + NLY
	fullHours = fullDays*24
	fullMinutes = fullHours*60
	fullSeconds = fullMinutes*60

	#flaga zezwolenia	
	allow = True
	#liczymy pełne lata, a na koncu odejujemy po 1 dniu z lat przestepnych
	return years, daysBetween, aY, bY, NLY, fullDays, allow, fullSeconds		
	
def	startAllow():
	try:
		allow = ageCalculating(dateOfBirth, actualDate, leapYears)[6]
	except TypeError:
		allow = False
	
	if (allow == True):
		print()
		print('Data urodzin: ', dateOfBirth)
		print('Data obecna: ', actualDate)	
		spam = ageCalculating(dateOfBirth, actualDate, leapYears)
		years = spam[0]
		daysBetween = spam[1]
		aY = spam[2]
		bY = spam[3]
		NLY = spam[4]
		fullDays = spam[5]
		fullSeconds = spam[7]	
			
		print()
		strY = int(str(years)[-1])
		if (strY > 1) and (strY < 5):
			print('Masz %s lata oraz %s dni.' % (years, daysBetween))
		elif (years == 1):
			print('Masz %s rok oraz %s dni.' % (years, daysBetween))
		elif (years == 0):
			pass
		else:
			print('Masz %s lat oraz %s dni.' % (years, daysBetween))	
		print('Żyjesz na tej planecie od %s dni.' % (fullDays))
		print('Twoj wiek wyrażony w sekundach, to %s sekund.' % fullSeconds)
	else:
		print('something went wrong! albo tak mialo byc')

#get data from user		
data = checkData()
dateOfBirth = data[0]
actualDate = data[1]		
leapYears = data[2]	

#start calculating		
startAllow()		
