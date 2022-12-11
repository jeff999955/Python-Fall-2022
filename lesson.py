import json
from typing import List

from question import Question


class Lesson:
    def __init__(self, name: str) -> None:
        self.name = name
        self._instructions: List[str] = []
        self._questions: List[Question] = []
        self._tutorials: List[str] = []

    def add_instruction(self, instruction: str):
        self._instructions.append(instruction)

    def show_instructions(self):
        for instruction in self._instructions:
            print(instruction)
            input("Press enter to continue...")

    def add_question(self, question: Question):
        self._questions.append(question)

    def show_questions(self):
        for question in self._questions:
            question.ask()
            if question.validate():
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {question.answer}.")
                question.show_tutorial()
            input("Press enter to continue...")

    def add_tutorial(self, link: str):
        self._tutorials.append(link)

    def show_tutorials(self):
        print("Tutorial:")
        for link in self._tutorials:
            print(f"\t{link}")

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4,
        )

    @staticmethod
    def from_json(self, data):
        self.name = data["name"]
        self._instructions = data["instructions"]
        self._questions = [
            Question.from_json(question) for question in data["questions"]
        ]
        self._tutorials = data["tutorials"]
        return self
