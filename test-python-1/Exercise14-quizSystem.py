questions_file = open('questions.txt', 'r')
question_list = [text_line.strip() for text_line in questions_file]
questions_file.close()
m = len(question_list)
n = 0
for line in question_list:
    question_answer = line.split('=')  # for 1+1=2 returns a list ["1+1", "2"]
    user_answer = input(f'{question_answer[0]}=')
    if user_answer == question_answer[1]:
        n += 1

result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {n}/{m}.')
result_file.close()
