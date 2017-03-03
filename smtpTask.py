#smtp by stranger 14.11.16r.
import time, smtplib, sys, socket
#działa dosyc poprawnie :)
#odnotowano poprawne wyslanie wiadomosci z servera smtp zarowno dla wp.pl oraz o2.pl 
def mail_smtp():
	#mialo sluzyc jako pojemnik dla atrybutow wiadomosci - haslo, host, etc
	maila_data = []
	
	print('Uwaga: musisz mieć włączoną usługę SMTP na swoim mailu\n')
	time.sleep(0.3)
	print("Za chwilę stworzysz wiadomość email. Podaj niezbędne dane: \n")
	#zmienna poprawnosci wpisywania danych
	correct = False
	
	while (correct == False):
		correct = True
		host = input('Poczta z której korzystasz -> dla wp.pl (1), dla o2.pl (2):\n')
		if (host == '1'):
			host = "smtp.wp.pl"
		elif (host == '2'):
			host = "poczta.o2.pl"
		else:
			correct = False	
		sender = input('Nadawca - pełny adres twojej poczty e-mail: \n')
		if (sender.find('@') == -1):
			correct = False
		password = input('Haslo twojej poczty: \n')
		#login = sender[:(sender.find('@'))] #jednak zbedny
		receiver = input('Adresat - pełny adres skrzynki odbiorcy: \n')
		if (receiver.find('@') == -1):
			correct = False
		subject = input('Temat e-maila: \n')
		main_text = input('Tresc maila: \n')
		if (correct == False):
			time.sleep(0.5)
			print('\nNiepoprawny host lub adres email.\n')
		else:
			time.sleep(0.5)
			print('\nDane wpisane względnie poprawnie. \n')
			break
		
	SenOrCan = input('Send email (S) oraz cancel(C) ? \n')
	SenOrCan = SenOrCan.lower()
	while (SenOrCan != "s") or (SenOrCan != "c"):
		if	(SenOrCan == "s"):
			print("To może zająć kilka chwil...")
			body = "\r\n".join(("From: %s" % sender,"To: %s" % receiver,"Subject: %s" % subject, "",main_text))
			try:
				server = smtplib.SMTP(host)
				server.login(sender, password)
				server.sendmail(sender, [receiver], body)
				server.quit()
				print("Wiadomość wysłana pomyślnie.")
				time.sleep(1)
				break
			except smtplib.SMTPAuthenticationError:
				#obsluga błędu; działa poprawnie 14.11.16r. g.: 00:46
				print('\nBledne dane, badz blad serwera. Sprobuj ponownie.')
				break
			except smtplib.SMTPServerDisconnected:
				print('\nPolaczenie przerwane przez komputer hosta.')
				time.sleep(1)
				break
			except socket.gaierror:
				print('\nProblem z połączeniem. Kończenie...')
				time.sleep(1)
				break
		elif (SenOrCan == "c"):
			print('Wysyłanie wiadomości anulowane...')
			break
		else:
			SenOrCan = input('Send email (S) oraz cancel(C) ? \n')
			SenOrCan = SenOrCan.lower()
	return print('zakonczono\n')
	
mail_smtp()	
	
	