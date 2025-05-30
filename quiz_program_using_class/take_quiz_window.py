import tkinter as tk
from tkinter import ttk, messagebox
from question_manager import QuestionManager
import random

class TakeQuizWindow:
    def __init__(self, root):
        self.quiz_window = tk.Toplevel(root)
        self.quiz_window.title("Take a Quiz")
        self.quiz_window.geometry("600x700")
        self.quiz_window.configure(bg="#f0f4f7")
        self.build_ui()

    def build_ui(self):
        tk.Label(self.quiz_window, text="Choose category to take quiz:",
                 bg="#f0f4f7", fg="#333", font=("Helvetica", 10, "bold")).pack(pady=5)
        self.quiz_category_var = tk.StringVar()
        ttk.Combobox(self.quiz_window, textvariable=self.quiz_category_var, values=["Math", "English", "Science", "Filipino"]).pack(pady=5)

        tk.Button(self.quiz_window, text="Start Quiz", command=self.load_quiz,
                  bg="#2196f3", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

        self.quiz_frame = tk.Frame(self.quiz_window, bg="#f0f4f7")
        self.quiz_frame.pack(pady=10, fill="both", expand=True)

    def load_quiz(self):
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        selected = self.quiz_category_var.get().lower()
        questions = QuestionManager.load(selected)

        if not questions:
            tk.Label(self.quiz_frame, text="No quiz available for this category.", fg="red").pack()
            return

        question = random.choice(questions)

        tk.Label(self.quiz_frame, text=f"Q: {question['text']}", font=("Helvetica", 11, "bold")).pack(pady=5)

        self.answer_var = tk.StringVar()

        for key in ['a', 'b', 'c', 'd']:
            tk.Radiobutton(
                self.quiz_frame,
                text=f"{key}) {question['choices'].get(key, '')}",
                variable=self.answer_var,
                value=key,
                font=("Helvetica", 10),
                bg="#f0f4f7"
            ).pack(anchor='w')

        tk.Button(self.quiz_frame, text="Submit", command=lambda: self.submit_answer(question),
                  bg="#4caf50", fg="white", padx=10, pady=2).pack(pady=10)

    def submit_answer(self, question):
        if self.answer_var.get() == "":
            messagebox.showwarning("No answer", "Please select an answer.")
            return
        if self.answer_var.get() == question['answer']:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong. The correct answer is: {question['answer']}")
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        tk.Label(self.quiz_frame, text="Quiz finished. You may close this window.", font=("Helvetica", 11)).pack(pady=10)