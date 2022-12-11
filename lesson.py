from question import Question


class Lesson:
    def __init__(self, name: str) -> None:
        self.name = name
        self.instructions = []
        self.questions = []

    def add_instruction(self, instruction: str):
        self.instructions.append(instruction)

    def show_instructions(self):
        for instruction in self.instructions:
            print(instruction)
            input("Press enter to continue...")

    def add_question(self, question: Question):
        self.questions.append(question)

    def show_questions(self):
        for question in self.questions:
            question.ask()
            if question.validate():
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is {question.answer}.")
                question.show_tutorial()
            input("Press enter to continue...")
