id = '0001'

new_id = int(id)+1
id_len = len(id)

new_id = f'{new_id:0{id_len}}'



print(new_id) # 0000000002

n = 141
print(f'{n:010}') # Preferred method, python >= 3.6