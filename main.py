import json

from lesson import Lesson
from question import MultipleChoiceQuestion


def select_lesson() -> Lesson:
    print("Which lesson would you like to take?\n\t1. Lesson 1\n\t2. Lesson 2")
    choice = int(input("Your choice: "))
    if choice in [1, 2]:
        with open(f"lesson{choice}.json") as fp:
            return Lesson.from_json(json.load(fp))
    else:
        raise ValueError("Invalid choice")


def start_lesson(lesson: Lesson) -> None:
    print(f"Starting lesson {lesson.name}")
    while True:
        print("1. Show instructions")
        print("2. Show questions")
        print("3. Show tutorials")
        print("4. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            lesson.show_instructions()
        elif choice == "2":
            lesson.show_questions()
        elif choice == "3":
            lesson.show_tutorials()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def main() -> None:
    print("Welcome to the Python lesson!")
    log_file = open("log.txt", "w+")
    while True:
        print("1. Start lesson")
        print("2. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            try:
                lesson = select_lesson()
            except Exception:
                print("Invalid choice for the lesson.")
            lesson.set_logger(log_file)
            start_lesson(lesson)
        elif choice == "2":
            break
        else:
            print("Invalid choice.")
    log_file.close()


if __name__ == "__main__":
    main()
