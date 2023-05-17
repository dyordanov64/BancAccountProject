# функция за въвеждане на коректна стойност за число и подканващо съобщение за това
def get_user_number(message : str, min : int, max : int)->int:
	while True :
		try:
			x = int(input(f'{message} [{min}..{max}]: '))
			if x >= min and x <= max :
				return x
		except:
			print('A correct value, please!!!')
# 			връща съобщение за грешка

# функция за въвеждане на стринг от цифри с определена дължина
def get_user_limited_string(message : str, min : str, max : str) -> str :
	while True :
		try :
			limited_string = input(f'{message} [{min}..{max}]: ')
			# проверка дали е въведен числов стринг с определена дължина
			if len(limited_string) == len(max) and int(limited_string) >= 0 :
				return limited_string
		except :
			print('въведете коректна стойност в диапазона [{min}..{max}]: ')

# Функция за създаване на нов акаунт
def new_account(acount_list) :
	#
	full_name = input('Enter your three names:')
	pin_code = get_user_limited_string('Please input a PIN of your choice: ','0000', '9999')
	value_deposit = get_user_number('Please input a value to deposit to start of account: ', 1 , 1000000000)
	# изчисляване на 10 разреден номер на новата сметка - 
	# към броя на записите в Списъка добавяме 1 и запълваме с 0 до 10 разряда
	account_num = str(len(acount_list)+1)
	while len(account_num) < 10 :
		account_num = '0' + account_num
		# Добавяме новия запис към текущия списък
	acount_list.append(
		{
		'account_number' : account_num,
		'account_owner_full_name' : full_name,
		'account_pin' : pin_code,
		'account_balance' : value_deposit
		}
	)

# изпълняване на транзакциите за теглене, внасяне и проверка на сметката на клиента
def bank_transaction(acount_list, transaction) :
	acount = acount_list[len(acount_list)-1] # взимане номера на последната сметка 
	# за да се изведе коректна подсказка за въвеждане на правилен номер на банкова сметка
	print(acount)

	acount_num = get_user_limited_string('Input account nomber:', '0000000001', acount['account_nomber'])
	for account in acount_list : # взимане на коректнатия запис "dictionary" от списъка
		if acount_num == account['account_nomber'] : # намиране на коректната банкова сметка от списъка
			pin_code = get_user_limited_string('Please input a PIN of your choice: ','0000', '9999') # след което клиента въвежда PIN
			if pin_code == account['pin_code'] : # при правилен пин се извършва конкретната операция
				if transaction == 'whithdraw' : # теглене
					amount = get_user_number('Input whithdraw amount: ', 1, account['account_balance'])
					account['account_balance'] -= amount
				elif transaction == 'deposit' : # депозит
					amount = get_user_number('Input deposit amount: ', 1, 1000000000)
					account['account_balance'] += amount
				else :  # и проверка на сметката
					print(f"Account Name is {account['full_name']}")
				print(f"Account balance is {account['account_balance']}")






