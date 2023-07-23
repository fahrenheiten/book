# # Прочесть остаток файла в одну строку
# with open('new.txt','rt') as file:
#     data = file.read()
# print(data)
# # Итерируем по строчкам файла
# with open('new.txt','rt') as file:
#     for line in file:
#         print(line)
# Пишем чанки (кусочки) текстовых данных
with open('new.txt','wt') as file:
    file.write(text1)
    file.write(text2)