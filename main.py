question_list = []

for question in question_list:
    question.ask()
    if question.validate():
        print("Correct!")
    else:
        print("Incorrect!")
