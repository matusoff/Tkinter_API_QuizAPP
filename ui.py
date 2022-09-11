from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    #the __init__ function will be called whenever we create a new object from this class
    # in this clas we will create the user interface (buttoms, layers etc)
    # the __init__ method does even know what is data type of the quiz_brain object that was passes here
    # so we can add parameter saying that quiz_brain object must be of data type of quiz_brain
    # in order to make it works we have to import from quiz_brain import Qizbrain class 
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
        #this line of code (43) is to back bg to white after give_feedback function 
        self.canvas.config(bg="white")

        #if there are remaining questions, user will go to the next one 
        if self.quiz.still_has_questions():
            #to get the score on the interface we need to config the score_label 
            # with the access a quiz method from QiuzBrain, so quiz.score 
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            #update canvas to change item which is self.question_text(line 19)
            self.canvas.itemconfig(self.question_text, text=q_text)
            #after we update the canvas we need to call this method in __init__
            #we do it in line 37
        
        else:
            self.canvas.itemconfig(self.question_text, text="You're reached the end of the quiz")
            #to disable the true or false buttons in the end of the quiz
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
      

    def true_pressed(self):
        #because we already have access to quiz_brain object in line 13,
        #so we can use it to get access to check_answer 
        #and to catch when we call the check_aswer method 
        # we return True or False in check_answer function inside QUizBrain class
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
        


