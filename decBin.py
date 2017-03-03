#funckja zwraca zakodowaną wiadomość w postaci bin lub hex

def binKoder(message, lenght=8):
	if (lenght % 1 == 0):
		pass
	else:
		series = 0
		return series, print('nieprawidlowa dlugosc klucza')
	def decBin(decimal):
		binNum = '0b' + '0'*(lenght-(len(bin(decimal))-2)) + bin(decimal)[2:]
		return binNum
			
	letters = []
	binaries = []
	series = ''
	for x in range(len(message)):
		letters.append(ord(message[x]))
	for x in range(len(letters)):
		binary = decBin(letters[x])
		binaries.append(binary)	
		#liczby przyciete w postaci ciagu
		series += binary[2:]
	seriesHex = hex(int(series))	
	return series, seriesHex, lenght

#dekodowanie
def dekoder(series, lenght=8):
	if (series == 0):
		return print('coś poszło nie tak')
	else:
		pass
	integers = []
	decrypt = ""
	series = str(series)
	divide = (len(series))/lenght
	if (divide % 1 == 0):
		for x in range(int(divide)):
			binar = '0b' + series[x*(lenght):(x+1)*(lenght)]
			integers.append(int(binar,2))
		for x in range(len(integers)):
			decrypt += chr(integers[x])
		return decrypt, integers
	else:
		print('zła długość klucza')
	
'''	
#ponizej znajduje sie przykladowe uzycie skryptu
message = 'to jest super tajna wiadomość'
code = binKoder(message,10)
series = code[0]
print(series,'\n')
'''

message = "Beware the bearers of FALSE gifts. Conduit CLOSING"
message = message.lower()
code = binKoder(message, 8)
series = code[0]
reversed = series[::-1]
seriesHex = code[1]

#print(series, '\n')
print("message: ", message, '\n')
print('hex: ', seriesHex)

decode = dekoder(series, 8)
decrypt = decode[0]

#print('integers: \n', decode[1])
#print('wiadomość: \n', decode[0])		
