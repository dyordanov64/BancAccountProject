from lib_1.custom_exceptions import NonExistentAccount, InvalidPin
from lib_1.my_IO import get_user_limited_string, get_user_number
from lib_1.validation import validate_pin

class Bank_Account :
	def __init__(self, account_nomber, full_name, pin_code, value_deposit):
		self.account_nomber = account_nomber
		self.full_name = full_name
		self.pin_code = pin_code
		self.value_deposit = value_deposit

# Функция за създаване на нов акаунт
	def new_account(self, acount_list) :
		#
		self.full_name = input('Enter your three names:')
		self.pin_code = get_user_limited_string('Please input a PIN of your choice: ','0000', '9999')
		self.value_deposit = get_user_number('Please input a value to deposit to start of account: ', 1 , 1000000000)
		# изчисляване на 10 разреден номер на новата сметка -
		# към броя на записите в Списъка добавяме 1 и запълваме с 0 до 10 разряда
		self.account_nomber = str(len(acount_list)+1)
		while len(self.account_nomber) < 10 :
			self.account_nomber = '0' + self.account_nomber

			# Добавяме новия запис към текущия списък
		acount_list.append(
			{
			'account_nomber' : self.account_nomber,
			'full_name' : self.full_name,
			'pin_code' : self.pin_code,
			'account_balance' : self.value_deposit
			}
		)

def find_account(account_list, account_number):
	for account in account_list:
		if account['account_nomber'] == account_number:
			return account

	raise NonExistentAccount(account_number)

	# # get account dict from account_list, filtered by 'account_nomber'
	# try:
	# 	account = next(filter(lambda acc: acc['account_nomber']==account_number, account_list))
	# 	return account
	# except:
	# 	raise NonExistentAccount(account_number)


def get_user_account(acount_list):
	acount_max_num = acount_list[-1]['account_nomber'] # взимане номера на последната сметка
	# за да се изведе коректна подсказка за въвеждане на правилен номер на банкова сметка
	user_account_number = get_user_limited_string('Input account nomber:', '0000000001', acount_max_num)

	account = find_account(acount_list, user_account_number)

	validate_pin(account)

	print(f'USER_ACCOUNT_NUMBER: {user_account_number}')

	return account

# изпълняване на транзакциите за теглене, внасяне и проверка на сметката на клиента
def bank_transaction(acount_list, transaction) :
	# get user account:
	try:
		account = get_user_account(acount_list)
		print(account)
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


