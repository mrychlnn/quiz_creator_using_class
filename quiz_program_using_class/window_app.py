import tkinter as tk
from add_question_window import AddQuestionWindow
from take_quiz_window import TakeQuizWindow

class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quizyowww Menu")
        self.root.geometry("400x300")
        self.root.configure(bg="#e3f2fd")
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Quizyowww", font=("Helvetica", 14, "bold"), bg="#e3f2fd").pack(pady=20)

        tk.Button(self.root, text="1. Enter questions", command=self.open_add_question_window,
                  bg="#4caf50", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)
        tk.Button(self.root, text="2. Take a Quiz", command=self.open_take_quiz_window,
                  bg="#2196f3", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)
        tk.Button(self.root, text="3. Exit the program", command=self.root.destroy,
                  bg="#f44336", fg="white", font=("Helvetica", 11), width=25).pack(pady=10)

    def open_add_question_window(self):
        AddQuestionWindow(self.root)

    def open_take_quiz_window(self):
        TakeQuizWindow(self.root)

    def run(self):
        self.root.mainloop()