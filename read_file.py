def remove_dot(substring):
	index = substring.find(".")
	substring[index] = "!"
	return index

def read_file():
	with open('referat.txt', 'r', encoding = "utf-8") as file:
		content = file.read()
	print(f'Длина строки: {len(content)} символов')
	list_content = content.split(' ')
	print(f'Файл содержит {len(list_content)} слов')
	content_new = content.replace('.', '!')
	print(content_new)
	with open('referat2.txt', 'w', encoding = "utf-8") as file:
		file.write(content_new)

if __name__ == "__main__":
	read_file()