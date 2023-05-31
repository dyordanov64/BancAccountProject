from lib_1.my_IO import get_user_limited_string

def validate_pin(account):
	user_pin_code = get_user_limited_string('Please input a PIN of your choice: ','0000', '9999')
	if user_pin_code!=account['pin_code']:
		raise InvalidPin(user_pin_code)