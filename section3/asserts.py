assert abs(-42) == 42
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')