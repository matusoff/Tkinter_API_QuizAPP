from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, heigh=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, 
            text=f"Some Question Text", width=250, 
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.score_label = Label(text="Score: 0")
        self.score_label.grid(column=1, row=0)
        self.score_label.config(fg="white", bg=THEME_COLOR, font=("Arial", 12, "normal"))

        false_image = PhotoImage(file=r"PROJECTS\100days_of_code\API_module\API_Trivia_Quiz\images\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        true_image = PhotoImage(file=r"PROJECTS\100days_of_code\API_module\API_Trivia_Quiz\images\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        
        else:
            self.canvas.itemconfig(self.question_text, text="You're reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
      

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)
        


