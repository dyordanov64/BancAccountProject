class NonExistentAccount(Exception):
	""" Raised when User Account does not exists"""
	def __init__(self, account_number) -> None:
		self.message = f'Account {account_number} does not exists!'
		super().__init__(self.message)

class InvalidPin(Exception):
	"""Raised when an invalid PIN is entered."""
	def __init__(self, pin) -> None:
		self.message = f'PIN: {pin} is invalid!'
		super().__init__(self.message)