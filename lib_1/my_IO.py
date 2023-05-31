
# функция за въвеждане на коректна стойност за число и подканващо съобщение за това
def get_user_number(message : str,min : int,max : int)->int:
	while True :
		try:
			x = int(input(f'{message} [{min}..{max}]: '))
			if x >= min and x <= max :
				return x
		except KeyboardInterrupt:
			# allow CTRL+C to work as expected, i.e. exit the program
			exit()
		except:
			print('A correct value, please!!!')

# функция за въвеждане на стринг от цифри с определена дължина
def get_user_limited_string(message : str, min : str, max : str) -> str :
	while True :
		try :
			limited_string = input(f'{message} [{min}..{max}]: ')
			# проверка дали е въведен числов стринг с определена дължина
			if len(limited_string) == len(max) and int(limited_string) >= 0 :
				return limited_string
		except KeyboardInterrupt:
			# allow CTRL+C to work as expected, i.e. exit the program
			exit()
		except :
			print('въведете коректна стойност в диапазона [{min}..{max}]: ')




