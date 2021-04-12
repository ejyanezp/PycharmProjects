import csv
import json


def write_to_file(output):
    csv_output = open('data_output.csv', 'w', newline='\n')
    writer = csv.writer(csv_output)
    writer.writerows(output)
    csv_output.close()


def read_from_file():
    csv_input = open('csv_file.txt', 'r')
    reader = csv.reader(csv_input)
    result = list(reader)
    csv_input.close()
    return result


my_list = read_from_file()
print(my_list)
dict_list = []
headers = ['club', 'city', 'country']
for elem in my_list:
    my_dict = {headers[i]: elem[i] for i in range(0, 3)}
    dict_list.append(my_dict)
print(dict_list)
write_to_file(my_list)

output_json_file = open('CRUDOLAPIsService', 'r')
json.dump(dict_list, output_json_file)
# Si no se cierra el archivo da error, es por ello que
# trabajar los archivos con el "with" es mejor (un context manager)
# al salir del "with" el archivo se cierra automaticamente (sin el close)
output_json_file.close()

