import pyperclip

usersString = pyperclip.paste()

print(" ")
arr = []
out = ""

for i in range(len(usersString)):
	arr.append(usersString[i])


changeENG = ["A", "a","B", "E", "e", "K", "H", "O", "o", "P", "p", "C", "c", "T", "X ", "x"]
changeRUS = ["А", "а", "В", "Е", "е", "К", "Н", "О", "о", "Р", "р", "С", "с", "Т", "Х", "х"]


for i in range(len(usersString)):
	if changeRUS.count(arr[i]) == 1:
		arr[i] = changeENG[changeRUS.index(arr[i])]


for j in range(len(arr)):
	out += arr[j]

pyperclip.copy(out)
print("Все готово, жмякниет Enter)")
input()