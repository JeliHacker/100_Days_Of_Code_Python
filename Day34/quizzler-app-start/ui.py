from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Amazon acquired Twitch in August 2014 for $970 million dollars.",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.guess_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.guess_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)
        self.canvas.config(bg="white")
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz! Your score was {self.quiz.score}/10.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def guess_true(self):
        is_right = self.quiz.check_answer("True")

        self.give_feedback(is_right)
        #
        # self.get_next_question()
        # self.score_label.config(text=f"Score: {self.quiz.score}")

    def guess_false(self):
        is_right = self.quiz.check_answer("False")

        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state=DISABLED)
        self.false_button.config(state=DISABLED)
        self.window.after(2000, self.get_next_question)

