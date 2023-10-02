import json
from pymongo import MongoClient
from pprint import PrettyPrinter
from lib_1.banc_account import Bank

def connect_to_atlas_cluster():
  # connect using connection string:
  # mongodb+srv://<username>:<password>@cluster0.xm0yw.mongodb.net/<dbname?>
  connection_string = 'mongodb+srv://4gumicom:P1hIZlJpOjXSxcaK@cluster0.fzpcsb9.mongodb.net/'

  return MongoClient(connection_string)

# connect to DB
bank_client = connect_to_atlas_cluster()

# Create 'BankAccount'
db = bank_client.BankAccounts

def create_users_from_lists():
	user_names = ['Maria2','Ivan2']
	user_balances = [1000, 400]

	for user in zip(user_names,user_balances):
		print(user,balance)
		db.Users.insert_one({
			"user": user,
			"balance":balance
		})

	print(list(zip(user_names,user_balances)))