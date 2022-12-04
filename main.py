class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def ask(self):
        answer = input(self.prompt)
        if answer == self.answer:
            return True
        return False


question_list = []

for question in question_list:
    if question.ask():
        print("Correct!")
    else:
        print("Incorrect!")
