windows_serial_number = "abc-def-ghi-jkl"

new_partial_variable_a = windows_serial_number[0:3]
new_partial_variable_b = windows_serial_number[4:7]
new_partial_variable_c = windows_serial_number[8:11]
new_partial_variable_d = windows_serial_number[12:15]

print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)



new_partial_variable_a = new_partial_variable_a.replace('abc' , 'aaa')
new_partial_variable_b = new_partial_variable_b.replace('def' , 'bbb')
new_partial_variable_c = new_partial_variable_c.replace('ghi' , 'ccc')
new_partial_variable_d = new_partial_variable_d.replace('jkl' , 'ddd')

print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)


encoded_windows_serial_number = new_partial_variable_a + '-' + new_partial_variable_b + '-' + new_partial_variable_c + '-' + new_partial_variable_d
print("Encoded serial number ahead : " + encoded_windows_serial_number)



