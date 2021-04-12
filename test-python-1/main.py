# my_file = open('data.txt', 'r')
# file_content = my_file.read()
# my_file.close()
#
# print(file_content)
#
# user_name = input('Enter your name: ')
# my_file_output = open('data2.txt', 'w')
# my_file_output.write(user_name)
# my_file_output.close()

friends = input('Enter three words separated by comma: ').split(',')
print(friends)

people_file = open('data.txt', 'r')
people_nearby = people_file.readlines()
people_file.close()

print(people_nearby)
people_nearby = [people.strip() for people in people_nearby if people.startswith('J')]
print(people_nearby)

people_nearby_set = set(people_nearby)
print(people_nearby_set)
friends_set = set(friends)
print(friends_set)

