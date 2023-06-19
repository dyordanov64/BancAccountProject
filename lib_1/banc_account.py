from lib_1.custom_exceptions import NonExistentAccount, InvalidPin
from lib_1.my_IO import get_user_limited_string, get_user_number
from lib_1.validation import validate_pin
from lib_1.MyData import account_list
import json

class Bank_Account :
	def __init__(self):
		self.new_account()

	# Функция за създаване на нов акаунт
	def new_account(self) :
		#
		self.full_name = input('Enter your three names:')
		self.pin_code = get_user_limited_string('Please input a PIN of your choice: ','0000', '9999')
		self.value_deposit = get_user_number('Please input a value to deposit to start of account: ', 1 , 1000000000)
		self.account_nomber = ''

	# прочитане на един запис за банкова сметка от файла json
	def read_acount_from_Json(self) :
		pass

	# запис на един запис за банкова сметка във файла json
	def write_account_to_json(self, account_list) :
		json_file = open('account.json', '+x')

		pass



class Bank:
	def __init__(self) -> None:
		# get accounts from json file
		#self.accounts = account_list
		accounts_file = open("accounts.json", "r")
		self.accounts = json.load(accounts_file)

	def create_new_account(self):
		account = Bank_Account()
		# TODO: fix it, check tmp.py
		x=int(self.accounts[-1]['account_nomber'])+1
		account.account_nomber = f'{x:010}'

		self.add_account(account)

	def add_account(self, account):
		# # Добавяме новия запис към текущия списък
		self.accounts.append(
			{
				'account_nomber' : account.account_nomber,
				'full_name' : account.full_name,
				'pin_code' : account.pin_code,
				'account_balance' : account.value_deposit
			}
		)

	# запис на целия списък от банкови сметки във json
	def accounts_to_json(self) :
		accounts_file = open("accounts.json", "w", encoding="UTF-8")
		# for account in self.accounts :
		json.dump(self.accounts, accounts_file)
		pass

	# четене на целия списък от банкови смети от json file
	def read_accounts_from (self) :
		# accounts_file = open("accounts.json", "r")
		# self.accounts = json.load(accounts_file)
		pass

		# връща номера на последната сметка в базата
	def get_user_account(self):
		acount_max_num = self.accounts[-1]['account_nomber'] # взимане номера на последната сметка
		# print(acount_max_num)
		# acount_max_num = acount_list[-1]['account_nomber'] # взимане номера на последната сметка
		# за да се изведе коректна подсказка за въвеждане на правилен номер на банкова сметка
		user_account_number = get_user_limited_string('Input account nomber:', '0000000001', acount_max_num)

		account = find_account(self.accounts, user_account_number)

		validate_pin(account)

		print(f'USER_ACCOUNT_NUMBER: {user_account_number}')

		return account
	
		# изпълняване на транзакциите за теглене, внасяне и проверка на сметката на клиента
	def bank_transaction( self, transaction) :
		# get user account:
		try:
			account = self.get_user_account()
			# print(account)
		except NonExistentAccount as e:
			print(e)
			return
		except InvalidPin as e:
			print(e)
			return
		except Exception as e:
			print("Ups, something went wrong:", e)
			return

		# do transaction
		if transaction == 'whithdraw' : # теглене
			amount = get_user_number('Input whithdraw amount: ', 1, account['account_balance'])
			account['account_balance'] -= amount
		elif transaction == 'deposit' : # депозит
			amount = get_user_number('Input deposit amount: ', 1, 1000000000)
			account['account_balance'] += amount
		else :  # и проверка на сметката
			print(f"Account Name is {account['full_name']}")

		print(f"Account balance is {account['account_balance']}")
		
def find_account(account_lists, account_number):
	for account in account_lists:
		if account['account_nomber'] == account_number:
			return account

	raise NonExistentAccount(account_number)


# def find_account(account_list, account_number):
# 	for account in account_list:
# 		if account['account_nomber'] == account_number:
# 			return account

# 	raise NonExistentAccount(account_number)

	# # get account dict from account_list, filtered by 'account_nomber'
	# try:
	# 	account = next(filter(lambda acc: acc['account_nomber']==account_number, account_list))
	# 	return account
	# except:
	# 	raise NonExistentAccount(account_number)


# def get_user_account(self):
# 	acount_max_num = self.accounts[-1]['account_nomber'] # взимане номера на последната сметка
# 	# acount_max_num = acount_list[-1]['account_nomber'] # взимане номера на последната сметка
# 	# за да се изведе коректна подсказка за въвеждане на правилен номер на банкова сметка
# 	user_account_number = get_user_limited_string('Input account nomber:', '0000000001', acount_max_num)

# 	account = find_account(self.accounts, user_account_number)

# 	validate_pin(account)

# 	print(f'USER_ACCOUNT_NUMBER: {user_account_number}')

# 	return account




