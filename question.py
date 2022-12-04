from typing import Iterable, Union


class Question:
    def __init__(
        self,
        prompt: str,
        answer: str,
        tutorial: Union[str, Iterable[str]] = None,
    ):
        self.prompt = prompt
        self.answer = answer
        self.response = None
        if isinstance(tutorial, str):
            self.tutorial = [tutorial]
        else:
            self.tutorial = [*tutorial]

    def ask(self):
        self.response = input(self.prompt)

    def validate(self):
        return self.response == self.answer

    def add_tutorial(self, link):
        self.tutorial.append(link)

    def show_tutorial(self):
        print("Tutorial:")
        for link in self.tutorial:
            print(f"\t{link}")


class MultipleChoiceQuestion(Question):
    def __init__(
        self,
        prompt: str,
        answer: str,
        choices: Iterable[str],
        tutorial: Union[str, Iterable[str]] = None,
    ):
        super(MultipleChoiceQuestion, self).__init__(prompt, answer, tutorial)
        self.choices = choices
        if self.answer not in self.choices:
            raise "Answer must be in choices"

    def ask(self):
        print(self.prompt)
        print("Choices: " + ",".join(self.choices))
        self.response = input("Your answer: ")
