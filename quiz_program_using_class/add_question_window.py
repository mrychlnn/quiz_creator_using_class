import tkinter as tk
from tkinter import ttk, messagebox
from question_manager import QuestionManager

class AddQuestionWindow:
    def __init__(self, root):
        self.add_window = tk.Toplevel(root)
        self.add_window.title("Quizyowww")
        self.add_window.geometry("600x700")
        self.add_window.configure(bg="#f0f4f7")
        self.build_ui()

    def build_ui(self):
        tk.Label(self.add_window, text="Choose category (Math, English, Science, Filipino)").pack(pady=5)
        self.category_var = tk.StringVar()
        ttk.Combobox(self.add_window, textvariable=self.category_var, values=["Math", "English", "Science", "Filipino"]).pack(pady=5)

        tk.Label(self.add_window, text="Enter the question:").pack()
        self.question_text = tk.Text(self.add_window, height=4, width=70)
        self.question_text.pack()

        self.entry_choice_a = self.create_entry("Choice a:")
        self.entry_choice_b = self.create_entry("Choice b:")
        self.entry_choice_c = self.create_entry("Choice c:")
        self.entry_choice_d = self.create_entry("Choice d:")

        tk.Label(self.add_window, text="Correct Answer (a, b , c, d):").pack()
        self.correct_answer_var = tk.StringVar()
        tk.Entry(self.add_window, textvariable=self.correct_answer_var, width=10).pack(pady=5)

        tk.Button(self.add_window, text="Save Question", command=self.save_question,
                  bg="#4caf50", fg="white", font=("Helvetica", 10, "bold")).pack(pady=10)

    def create_entry(self, label):
        tk.Label(self.add_window, text=label).pack()
        entry = tk.Entry(self.add_window, width=70)
        entry.pack()
        return entry

    def save_question(self):
        category = self.category_var.get().lower()
        if category not in ["math", "english", "science", "filipino"]:
            messagebox.showinfo("Error", "Choose a valid category.")
            return

        question = self.question_text.get("1.0", tk.END).strip()
        choice_a = self.entry_choice_a.get().strip()
        choice_b = self.entry_choice_b.get().strip()
        choice_c = self.entry_choice_c.get().strip()
        choice_d = self.entry_choice_d.get().strip()
        correct_answer = self.correct_answer_var.get().strip().lower()

        if not all([question, choice_a, choice_b, choice_c, choice_d]) or correct_answer not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Please fill the fields and choose a valid correct answer (a-d).")
            return

        QuestionManager.save(category, question, choice_a, choice_b, choice_c, choice_d, correct_answer)
        messagebox.showinfo("Saved", f"Question saved to {category}.txt")
        self.clear_fields()

    def clear_fields(self):
        self.question_text.delete("1.0", tk.END)
        self.entry_choice_a.delete(0, tk.END)
        self.entry_choice_b.delete(0, tk.END)
        self.entry_choice_c.delete(0, tk.END)
        self.entry_choice_d.delete(0, tk.END)
        self.correct_answer_var.set("")