import csv


def csv_read_write():
	list_dict = [
		{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        	{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        	{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
       		]
	with open('dict.csv', 'w', encoding = "windows-1251", newline = '') as file_csv:
		fields = ['name', 'age', 'job']
		writer = csv.DictWriter(file_csv, fields, delimiter=';')
		writer.writeheader()
		for employee in list_dict:
			writer.writerow(employee)


if __name__ == "__main__":
	csv_read_write()
