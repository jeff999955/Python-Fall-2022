from question import MultipleChoiceQuestion


question_list = [
    MultipleChoiceQuestion(
        prompt="print(type(0.56)) 顯示的結果為何?",
        answer="float",
        choices=["int", "float", "str", "bool"],
    ),
]

for question in question_list:
    question.ask()
    if question.validate():
        print("Correct!")
    else:
        print("Incorrect!")
