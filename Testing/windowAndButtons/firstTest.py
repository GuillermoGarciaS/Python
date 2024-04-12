import tkinter as tk
from tkinter import ttk, messagebox


class Questionnaire:
    def __init__(self, master):
        self.master = master
        self.current_question = 0
        self.questions = [
            "Do you love floppa?",
            "What about sogga?",
            "Which one do you love the most?"
        ]

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure('TButton', background='white', foreground='black')
        self.style.configure('TLabel', background='white', foreground='black')

        self.style.configure('TLabel', font=('Times New Roman', 14))  # Corrected typo in 'TLabel'
        self.style.configure('TButton', font=[('Times New Roman', 12)])

        self.answer_entries = []

        self.question_label = tk.Label(master, text=self.questions[self.current_question])
        self.question_label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.prev_button = tk.Button(master, text="<", command=self.prev_question)
        self.prev_button.pack(side=tk.LEFT)

        self.prev_button = tk.Button(master, text=">", command=self.next_question)
        self.prev_button.pack(side=tk.RIGHT)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answers)
        self.submit_button.pack(side=tk.BOTTOM)

    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.question_label.config(text=self.questions[self.current_question])

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.question_label.config(text=self.questions[self.current_question])

    def submit_answers(self):
        answers = [entry.get() for entry in self.answer_entries]
        messagebox.showinfo("Answers", "\n".join(answers))

    def show_answers(self):
        answers = self.submit_answers()

        answer_window = tk.Toplevel(self.master)
        answer_window.title = ("Answers")

        for i, answer in enumerate(answers, start=1):
            answer_label = tk.Label(answer_window, text=f"Question{i}: {answer}", font=('Times New Roman', 12))
            answer_label.pack()

        answers = [self.answer_entry.get()]
        messagebox.showinfo("Answers", "\n".join(answers))
        answer_window.destroy()


def main():
    root = tk.Tk()
    app = Questionnaire(root)
    root.mainloop()



if __name__ == "__main__":
    main()
