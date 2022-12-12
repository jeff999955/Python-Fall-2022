import json
from typing import Dict, Iterable, Union


class Question:
    def __init__(
        self,
        prompt: str,
        answer: str,
    ) -> None:
        self.prompt = prompt
        self.answer = answer
        self.response = None

    def ask(self):
        self.response = input(self.prompt)

    def validate(self):
        return self.response == self.answer

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4,
        )

    @staticmethod
    def from_json(data: Dict):
        return Question(
            prompt=data["prompt"],
            answer=data["answer"],
        )


class MultipleChoiceQuestion(Question):
    def __init__(
        self,
        prompt: str,
        answer: str,
        choices: Iterable[str],
    ):
        super(MultipleChoiceQuestion, self).__init__(prompt, answer)
        self.choices = choices
        if self.answer not in self.choices:
            raise "Answer must be in choices"

    def ask(self):
        print(self.prompt)
        print("Choices: " + ",".join(self.choices))
        self.response = input("Your answer: ")

    @staticmethod
    def from_json(data: Dict):
        return MultipleChoiceQuestion(
            prompt=data["prompt"],
            answer=data["answer"],
            choices=data["choices"],
        )
