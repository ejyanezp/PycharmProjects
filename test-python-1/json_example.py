import json

json_file = open('testdata.json', 'r')
file_content = json.load(json_file)
json_file.close()

print(file_content)
print(file_content['claveTransactions'][0]['terminalDescription'])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

output_json_file = open('output.json', 'w')
json.dump(cars, output_json_file)
