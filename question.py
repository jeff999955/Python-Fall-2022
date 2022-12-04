class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.response = None

    def ask(self):
        self.response = input(self.prompt)

    def validate(self):
        return self.response == self.answer


class MultipleChoiceQuestion(Question):
    def __init__(self, prompt, answer, choices):
        super().__init__(prompt, answer)
        self.choices = choices
        if self.answer not in self.choices:
            raise "Answer must be in choices"

    def ask(self):
        print(self.prompt)
        print(",".join(self.choices))
        self.response = input("Your answer: ")
