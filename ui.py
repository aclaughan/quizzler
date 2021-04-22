from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.win = Tk()
        self.win.title("Quizzler")
        self.win.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="score: 0",
            fg="white",
            bg=THEME_COLOR,
            anchor = "w"
        )
        self.score_label.grid(row=0, column=0,columnspan=2)

        self.category_label = Label(
            text="category: ",
            fg="white",
            bg=THEME_COLOR,
            anchor = "w"
        )
        self.category_label.grid(row=1, column=0,columnspan=2)

        self.difficulty_label = Label(
            text="difficulty: ",
            fg="white",
            bg=THEME_COLOR,
            anchor = "w"
        )
        self.difficulty_label.grid(row=2, column=0,columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text="placeholder",
            fill=THEME_COLOR,
            font = (
                "Ariel",
                20,
                "italic"
            )
        )
        self.canvas.grid(row=3,column=0,columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.t_button
        )
        self.true_button.grid(row=4,column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.f_button
        )
        self.false_button.grid(row=4,column=1)

        self.get_next_question()



        self.win.mainloop()


    def get_next_question(self):
        q_text = self.quiz.question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.category_label.config(
            text=f"score: {self.quiz.score}"
        )

        self.category_label.config(
            text=f"category: {self.quiz.category()}"
        )
        self.difficulty_label.config(
            text=f"difficulty: {self.quiz.difficulty()}"
        )

    def t_button(self):
        self.feedback(self.quiz.is_correct(answer='True'))

    def f_button(self):
        self.feedback(self.quiz.is_correct(answer='False'))

    def feedback(self, answer: str):
        self.canvas.config(bg="blue")
        self.win.after(1000)
        self.canvas.config(bg="white")
        self.get_next_question()