#!/usr/bin/python3

# Задание 1

def str_to_byte(arr):
    for i in range(len(arr)):
        arr[i] = ord(arr[i])


def byte_to_str(arr):
    for i in range(len(arr)):
        arr[i] = chr(arr[i])


s = list(input("Введите строку символов: "))
str_to_byte(s)
print("Ваша строка в виде кодов символов:", s)
byte_to_str(s)
print("Ваша строка (расшифрованная из кодов символов):", s)

# Задание 2

input_file = open('Input.txt', 'r')
output_file = open('Output.txt', 'w')
ethanol = 0
try:
    s = input_file.readline().split()
    molecule_C = int(s[0])
    molecule_H = int(s[1])
    molecule_O = int(s[2])
    while True:
        if molecule_C >= 2 and molecule_H >= 6 and molecule_O >= 1:
            ethanol += 1
            molecule_C -= 2
            molecule_H -= 6
            molecule_O -= 1
        else:
            break
except:
    print("Данные в файле не в нужном формате (Кол-во молекул C H O)")
output_file.write(str(ethanol))
input_file.close()
output_file.close()
