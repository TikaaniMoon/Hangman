import os
clear = lambda: os.system

print('Привет! Я загадал слово, твоя задача - угадать его по буквам.')
input('*Нажми Enter, чтобы продолжить*')
clear()
print('Поехали!')

word = 'трагикомедия'

for symb in word:
    print(symb, end=' ')