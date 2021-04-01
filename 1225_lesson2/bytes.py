# байты
print(b'text')
print('текст'.encode('utf-8'))
print(bytes('text', encoding='utf-8'))
print(bytes([10, 20, 30]))

my_barray = bytearray(b"some test")
print(my_barray)
print(my_barray[0], my_barray[1])

my_byte = 'текст'.encode('utf-8')
print(my_byte)
print(my_byte.decode())
