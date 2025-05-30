from question import Question

class QuizManager:
    def __init__(self):
        self.categories = ["math", "english", "science", "filipino"]

    def show_menu(self):
        print("\nMenu:")
        print("1. Enter a question (or another question/s)")
        print("2. Exit the program")

    def handle_input(self):
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1 or 2): ")

            if choice == "2":
                print("\nExiting the program... The entered data saved.")
                break

            if choice == "1":
                print("\nChoose a category for the quiz (Math, English, Science, Filipino)")
                category = input("Enter the category: ").lower()

                if category not in self.categories:
                    print("\nInvalid category. Choose from Math, English, Science, or Filipino.")
                    continue

                file_name = f"{category}.txt"

                try:
                    num = int(input("\nHow many question/s do you want to enter? "))
                except ValueError:
                    print("Invalid number.")
                    continue

                for all_questions in range(num):
                    print(f"\nQuestion {all_questions + 1} of {num}")
                    question = input("Enter the question: ")
                    choice_a = input("Enter the choice a: ")
                    choice_b = input("Enter the choice b: ")
                    choice_c = input("Enter the choice c: ")
                    choice_d = input("Enter the choice d: ")
                    correct_answer = input("What is the correct answer (a, b, c, d)? ")

                    questions = Question(question, choice_a, choice_b, choice_c, choice_d, correct_answer)

                    with open(file_name, "a") as saving_file:
                        saving_file.write(questions.format_question())

                    print(f"\nThe entered question/s saved to {file_name}!")
            else:
                print("\nInvalid input. Choose between 1 or 2.")