import os

class QuestionManager:
    @staticmethod
    def save(category, question, choice_a, choice_b, choice_c, choice_d, correct_answer):
        file_name = f"{category}.txt"
        saving_file = open(file_name, "a")
        saving_file.write(f"Question: {question}\n")
        saving_file.write(f"a) {choice_a}\n")
        saving_file.write(f"b) {choice_b}\n")
        saving_file.write(f"c) {choice_c}\n")
        saving_file.write(f"d) {choice_d}\n")
        saving_file.write(f"Correct answer: {correct_answer}\n")
        saving_file.write("-----\n")
        saving_file.close()

    @staticmethod
    def load(category):
        file_name = f"{category}.txt"
        if not os.path.exists(file_name):
            return []

        with open(file_name, "r") as file:
            blocks = file.read().strip().split("-----\n")

        questions = []
        for block in blocks:
            if not block.strip():
                continue
            lines = block.strip().split("\n")
            question = {"text": "", "choices": {}, "answer": ""}
            for line in lines:
                if line.startswith("Question:"):
                    question["text"] = line[9:].strip()
                elif line.startswith(("a)", "b)", "c)", "d)")):
                    question["choices"][line[0]] = line[3:].strip()
                elif line.startswith("Correct answer:"):
                    question["answer"] = line.split(":")[1].strip()
            questions.append(question)
        return questions