class Question:
    def __init__(self, question, choice_a, choice_b, choice_c, choice_d, correct_answer):
        self.question = question
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
        self.correct_answer = correct_answer

    def format_question(self):
        return (
            f"Question: {self.question}\n"
            f"a) {self.choice_a}\n"
            f"b) {self.choice_b}\n"
            f"c) {self.choice_c}\n"
            f"d) {self.choice_d}\n"
            f"Correct answer: {self.correct_answer}\n"
            "-----\n"
        )