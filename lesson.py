import json
from datetime import datetime
from io import TextIOWrapper
from typing import Dict, List

from question import MultipleChoiceQuestion, Question


class Lesson:
    def __init__(self, name: str) -> None:
        self.name = name
        self._instructions: List[str] = []
        self._questions: List[Question] = []
        self._tutorials: List[str] = []
        self._logger = None

    def add_instruction(self, instruction: str):
        self._instructions.append(instruction)

    def show_instructions(self):
        for instruction in self._instructions:
            print(instruction)
            input("Press enter to continue...")

    def add_question(self, question: Question):
        self._questions.append(question)

    def show_questions(self):
        # TODO: select 3 out of 5 questions
        for question in self._questions:
            question.ask()
            is_correct = question.validate()
            if is_correct:
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {question.answer}.")

            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=self._logger)
            print(question.prompt, file=self._logger)
            print("Correct" if is_correct else "Incorrect", end=", ", file=self._logger)
            print(question.response, file=self._logger)
            self._logger.flush()
            input("Press enter to continue...")

    def add_tutorial(self, link: str):
        self._tutorials.append(link)

    def show_tutorials(self):
        print("Tutorial:")
        for link in self._tutorials:
            print(f"\t{link}")

    def to_json(self):
        def beautify(data: Dict) -> Dict:
            return {key.lstrip("_"): value for key, value in data.items()}

        return json.dumps(
            self,
            default=lambda o: beautify(o.__dict__),
            sort_keys=True,
            indent=4,
        )

    @staticmethod
    def from_json(data: Dict):
        ret = Lesson(name=data["name"])
        for instruction in data["instructions"]:
            ret.add_instruction(instruction)
        for question in data["questions"]:
            ret.add_question(MultipleChoiceQuestion.from_json(question))
        for tutorial in data["tutorials"]:
            ret.add_tutorial(tutorial)
        return ret

    def set_logger(self, fp: TextIOWrapper):
        self._logger = fp
