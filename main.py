#Написать программу, которая: Запрашивает у пользователя строку для поиска. Находит и выводит все строки, которые содержат искомую подстроку, а также их количество из следующего файла.Сортирует найденные строки в порядке их длины (от самой короткой к самой длинной) и выводит их.
str=input("Введите строку для поиска:")
with open('text.txt', 'r', encoding= "Windows 1251") as text:
    lines=text.readlines()
list_str=[]
for line in lines:
    if str in line:
        list_str.append(line.strip())
len_str=len(list_str)
print("Количество строк с искомой подстрокой:",len_str)
for line in sorted(list_str, key=len):
    print(line)