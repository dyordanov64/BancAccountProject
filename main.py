# Проект 5 Управление на банкова сметка
# Описание:
# Проектът представлява обикновена банкова система. Той съдържа само
# административна част, без да се дава възможност на потребителя да влиза в система с
# потребителско име и парола. Административната част включва всички основни
# функции: създаване на нов акаунт, преглед на записа на притежателите на акаунти,
# теглене и депозит на сума, запитване за салдо. Потребителят трябва лесно да може да
# проверява общите записи на банковата сметка. Потребителят може да създаде акаунт,
# като предостави първоначална сума за депозиране. Той може да депозира и тегли пари
# само като предостави номера на потребителската си сметка и въведе сума.
# Потребителят може да проверява за клиенти и техният баланс по сметка.


import os
from time import sleep
import lib_1.my_IO as io
# import lib_1.banc_account as ba
from lib_1.banc_account import Bank
import lib_1.MyData as myd

# define our clear function
def clear_screen():
	# for windows
	if os.name == 'nt':
		_ = os.system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = os.system('clear')


#  ----Изработване на главното меню
def show_actions(line_width):
	print('='*line_width)
	print('='*line_width)
	print(f'---- {"Welcome to Times Bank":^{line_width-10}s} ----')
	print('*'*line_width)
	print(f'=<< {"1. Open new bank acount":<{line_width-8}s} >>=')
	print(f'=<< {"2. Whithdraw Money":<{line_width-8}s} >>=')
	print(f'=<< {"3. Deposit Money":<{line_width-8}s} >>=')
	print(f'=<< {"4. Check Customers & Balance":<{line_width-8}s} >>=')
	print(f'=<< {"5. Exit/Quit":<{line_width-8}s} >>=')
	print('*'*line_width)



bank = Bank()
print(bank.accounts)

while True :
	show_actions(60)
	choice = io.get_user_number('Input your choice: ', 1 , 5)
	print(choice)
	if choice == 1 :
		bank.create_new_account()
		bank.accounts_to_json()
		# print(bank.accounts)

		#exit()
	elif choice == 2 :
		bank.bank_transaction('whithdraw')
		bank.accounts_to_json()
	elif choice == 3 :
		bank.bank_transaction('deposit')
		bank.accounts_to_json()
	elif choice == 4 :
		bank.bank_transaction('check')
	else : 
		bank.accounts_to_json()
		quit()

	input('Press any key to continue: ')
	#sleep(5)
	#clear_screen()
	# print('test')
