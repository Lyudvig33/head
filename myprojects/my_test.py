def my_split(mstr):
    arr = []
    start = 0
    for i in range(len(mstr)):
        if mstr[i] == (','):
            arr.append(mstr[start:i])
            start = i
    arr.append(mstr[start:])
    return arr


mstr = "hello,good,world"

result = my_split(mstr)
print(result)





# if is_continue == False:
    #     root.destroy()
    #     return
    
    
    
    
    
    
"""This is a Who Wants To Be A Millionaire (Quiz Game).
It is built using the Tkinter module of Python.

Authore Lyudvig asoyan

In this game, the contestant's goal is to answer 15 multiple-choice
questions correctly in a row to win a cash prize.
To assist contestants in answering the questions correctly,
there are three lifelines available.
Date 30.05.2024
"""

# import library Tkinter all methods
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import json
import random
import pyttsx3



# The code part that opens user name window
root_name = Tk()
root_name.geometry("400x250")
root_name.title("User Name")
root_name.config(bg="black")
entry_name = Entry(
    root_name, width=30, background="white", fg="black", font=("arial", 13, "bold")
)
entry_name.pack(pady=40)


# The button that register the user
def on_submit():
    global username
    username = entry_name.get()
    root_name.destroy()

    return username


# The function to parse txt file to json
def questions_answers_txt():
    with open("questions_answers.txt", "r") as file:
        content = json.loads(file.read())

        return content





#  The fucntion to register
def user_name():
    global root_name, on_submit
    submit_button = Button(root_name, text="Enter", command=on_submit)
    submit_button.pack()

    root_name.mainloop()


user_name()




#  The function to create main window
def create_window():
    global root
    root = Tk()
    root.geometry("1270x652")
    root.title("Who wants to be a Millionaire, by Lyudvig Asoyan")
    root.config(bg="black")

    return root


# The function to create objects positions
def create_positions(root):
    leftframe = Frame(root, bg="black", padx=90)
    leftframe.grid(row=0, column=0)

    topframe = Frame(leftframe, bg="black", pady=-28)
    topframe.grid(row=0, column=0)

    centerframe = Frame(leftframe, bg="black", pady=-30)
    centerframe.grid(row=1, column=0)

    bottomframe = Frame(leftframe, bg="black")
    bottomframe.grid(row=2, column=0)

    rightframe = Frame(root, pady=30, padx=30, bd=0, background="black")
    rightframe.grid(row=0, column=1)

    return topframe, centerframe, rightframe, bottomframe


# The function to render images and buttons
def put_images_and_buttons(topframe, centerframe, rightframe, bottomframe):

    # The images should be global keep in memory
    global help50_50, audience_help, friend_call, game_logo, amount_image, questions_board, button_for50

    # The image for 50/50 help
    help50_50 = PhotoImage(file="public/images/50-50.png")

    button_for50 = Button(
        topframe,
        image=help50_50,
        text=str("50-50"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
    )

    button_for50.grid(row=0, column=0)
    button_for50.bind("<Button-1>", check_helps)

    # The image for audience help
    audience_help = PhotoImage(file="public/images/audiencePole.png")
    button_for_audience = Button(
        topframe,
        image=audience_help,
        text=str("audience_help"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
    )

    button_for_audience.grid(row=0, column=1)
    button_for_audience.bind("<Button-1>", check_helps)

    # The image for friends call help
    friend_call = PhotoImage(file="public/images/phoneAFriend.png")
    button_call = Button(
        topframe,
        image=friend_call,
        text=str("friend_call"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
    )
    button_call.grid(row=0, column=2)
    button_call.bind("<Button-1>", check_helps)

    # The image for icon of millionaire game
    game_logo = PhotoImage(file="/public/images/center.png")
    button_for_logo = Button(
        centerframe,
        image=game_logo,
        bg="black",
        bd=0,
        activebackground="black",
        width=360,
        height=250,
        highlightbackground="black",
    )
    button_for_logo.grid(row=0, column=0)

    # The image for amount of user
    amount_image = PhotoImage(file="public/images/Picture0.png")
    amount_lable = Label(rightframe, image=amount_image, bg="black")
    amount_lable.grid(row=0, column=0)

    # The image for questions board
    questions_board = PhotoImage(file="public/images/lay.png")
    questions_label = Label(bottomframe, image=questions_board, background="black")
    questions_label.grid(row=0, column=0)


# The coordinates of the answers ans Variants A,B,C,D
answers_places = {
    "A": {"x": 60, "y": 105},
    "B": {"x": 330, "y": 105},
    "C": {"x": 60, "y": 185},
    "D": {"x": 330, "y": 185},
}

# congig for questions ans answers
configs = {"questionNumber": 0, "options": [], "questionsCount": 15}


# The function for places questions and answers
def places_questions_and_answers(bottomframe):

    global quest_answ_right_ans, question_area, right_answer,answers

    question_area = Text(
        bottomframe,
        font=("arial", 18, "bold"),
        width=34,
        height=2,
        wrap="word",
        bg="black",
        fg="white",
        bd=0,
        highlightbackground="black",
    )
    question_area.place(x=70, y=10)
    questions = questions_answers_txt()

    # The logic to put and delete questions and answers
    quest_answ_right_ans = questions[configs["questionNumber"]]
    answers = quest_answ_right_ans["answers"]
    question = quest_answ_right_ans["question"]

    right_answer = quest_answ_right_ans["rightAnswer"]

    configs["right_answer"] = right_answer
    question_area.insert(END, str(question))

    for key in answers:
        answer = answers[key]

        x = answers_places[key]["x"]
        y = answers_places[key]["y"]

        option_button = Button(
            bottomframe,
            text=str(key + ": " + answer),
            font=("arial", 16, "bold"),
            bg="black",
            fg="white",
            bd=0,
            activebackground="black",
            highlightbackground="black",
            activeforeground="white",
            cursor="hand2",
        )

        option_button.place(x=x, y=y)
        option_button.bind("<Button-1>", check_right_and_wrong_answers)
        configs["options"].append(option_button)


# The function for check right answers and wrong answers and game over root, and you win root

def check_right_and_wrong_answers(event):
    global is_continue, correct_answer_count
    correct_answer_count = 0
    
    global amount_image, is_correct

    value = event.widget["text"]
    answer = value.split(":")[0]
    is_correct = answer == configs["right_answer"]
    
    configs["questionNumber"] = configs["questionNumber"] + 1
    if is_correct:
        correct_answer_count += 1
        
        for i in configs["options"]:
            i.destroy()

        # function for destroy help bar
        if "help_audience" in configs:
            for key in configs["help_audience"]:
                key.destroy()
        if "help_audience" in configs:
            del configs["help_audience"]

        # function to show next amount picture
        amount_image = PhotoImage(
            file="public/images/Picture" + str(configs["questionNumber"]) + ".png"
        )
        amount_lable = Label(rightframe, image=amount_image, bg="black")
        amount_lable.grid(row=0, column=0)

        # clear answers board for next answers
        configs["options"] = []

        # You win root window and winning count 
        if configs["questionNumber"] == configs["questionsCount"]:
            root2 = Toplevel()
            root2.config(bg="black")
            root2.geometry("700x400")
            img_lable = Label(root2, image=game_logo, bd=0)
            img_lable.pack()
            top_users_and_amount_winning()
            win_label = Label(
                root2,
                text= f"Congratulations!!! \nThe winning amount is {winning}",
                font=("arial", 30, "bold"),
                bg="black",
                bd=0,
                fg="white",
            )
            win_label.pack()
            root2.mainloop()
        else:
            question_area.delete(1.0, END)

            places_questions_and_answers(bottomframe)

    else:
        # create you lose window and winning count
        root1 = Toplevel()
        root1.config(bg="black")
        root1.geometry("700x400")
        img_lable = Label(root1, image=game_logo, bd=0)
        img_lable.pack()
        top_users_and_amount_winning()
        lose_label = Label(
            root1,
            text= f"Congratulations!! \nThe winning amount is {winning}",
            font=("arial", 30, "bold"),
            bg="black",
            bd=0,
            fg="white",
        )
        lose_label.pack()
        is_continue = False
        root1.mainloop()


# The funtion for helps
def check_helps(event):
    value = event.widget["text"]

    match value:
        case "50-50":
            help_50_50()
        case "audience_help":
            help_audience()
        case "friend_call":
            call_friend()
    
        

        
            

# The funtion for 50/50 help
def help_50_50():
    global button_for50X

    variants = {"A": 0, "B": 1, "C": 2, "D": 3}

    # Get the index of the correct answer from the configurations
    rightAnswerindex = variants[configs["right_answer"]]

    # Choose a random incorrect answer to remove
    randomWrongAnswer1 = random.choice([i for i in range(4) if i != rightAnswerindex])

    # Calculate the indices of remaining options after removing the first incorrect answer
    remaining_indices = [
        i for i in range(4) if i != randomWrongAnswer1 and i != rightAnswerindex
    ]

    # Choose a second random incorrect answer to remove from the remaining options
    randomWrongAnswer2 = random.choice(remaining_indices)

    # Loop through the options and destroy the widgets corresponding to the two incorrect answers
    for k, v in enumerate(configs["options"]):
        if k != rightAnswerindex and k != randomWrongAnswer2:
            v.destroy()

    # function for replace image 50/50X
    button_for50X = PhotoImage(file="public/images/50-50-X.png")

    button50X = Button(
        topframe,
        image=button_for50X,
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,
    )
    button50X.grid(row=0, column=0)


# function for help_audience
def help_audience():
    global audience_helpX, right_answer, help_bar, variants
    # coordinates for scales and variants
    help_bar_and_variants = {
        "A": {"scale": {"x": 580, "y": 240}, "letter": {"x": 580, "y": 190}},
        "B": {"scale": {"x": 620, "y": 240}, "letter": {"x": 620, "y": 190}},
        "C": {"scale": {"x": 660, "y": 240}, "letter": {"x": 660, "y": 190}},
        "D": {"scale": {"x": 700, "y": 240}, "letter": {"x": 700, "y": 190}},
    }

    # append help_bar and variants in configs, to destroy after answering
    configs["help_audience"] = []
    percentage = {}
    wrong_answer_sum = 0

    # the loop for put help_bar and variants in click help_audience
    for key, value in help_bar_and_variants.items():

        # help_bar percents for right answer
        if key != right_answer:
            percent = random.randint(1, 25)
            percentage[key] = percent
            wrong_answer_sum += percent

    for key, value in help_bar_and_variants.items():

        if right_answer == key:
            percent = 100 - wrong_answer_sum
            percentage[key] = percent

        scaleX = value["scale"]["x"]
        scaleY = value["scale"]["y"]

        # function to make the the help scale tint green
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "green.Horizontal.TProgressbar", foreground="green", background="green"
        )

        help_bar = Progressbar(
            root, orient=VERTICAL, length=120, style="green.Horizontal.TProgressbar"
        )
        help_bar.place(x=scaleX, y=scaleY)
        help_bar.config(value=percentage[key])

        configs["help_audience"].append(help_bar)

        letterX = value["letter"]["x"]
        letterY = value["letter"]["y"]

        variants = Label(
            root, text=key, font=("arial", 20, "bold"), bg="black", fg="white"
        )
        variants.place(x=letterX, y=letterY)

        configs["help_audience"].append(variants)

    # replace image audience_help and unplug that button
    audience_helpX = PhotoImage(file="public/images/audiencePoleX.png")
    button_for_audience = Button(
        topframe,
        image=audience_helpX,
        text=str("audience_help"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,
    )
    button_for_audience.grid(row=0, column=1)

#function for call friend help
def call_friend():
    global friend_call_helpX,right_answer
    #replace image call firend
    friend_call_helpX = PhotoImage(file="public/images/phoneAFriendX.png")
    firend_call = Button(
        topframe,
        image=friend_call_helpX,
        text=str("friend_call"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,
    )

    firend_call.grid(row=0, column=2)

    # library pyttxs3 text speach
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',170)
    engine.setProperty('voices',voices[1].id)
    
    
    # speak right answer when click call firend icon
    engine.say(f"i think correct answer is {right_answer},{answers[right_answer]}")
    engine.runAndWait()


# function for show top users and their winnings
def top_users_and_amount_winning():
    global winning

    list_of_amount_win = [0,1000,32000,1000000]
    if correct_answer_count < 5:
        winning = list_of_amount_win[0]
        
    elif correct_answer_count < 10:
        winning = list_of_amount_win[1]
        
    elif correct_answer_count < 15:
        winning = list_of_amount_win[2]
    else:
        winning = list_of_amount_win[3]
        
    # write and save users in txt file 
    with open('top_users.txt','+a') as users:
        users.write(f"{username}:{winning}:{correct_answer_count}\n")
        
    # read and sort users by their right answers count
    with open('top_users.txt','r+') as users:
        final_leader_board = []
        lider_board = users.readlines()
        for i in lider_board:
            el = i.strip('\n').split(':')
            el[2] = int(el[2]) 
            final_leader_board.append(el)
        final_leader_board.sort(key=lambda x:x[2],reverse=True)
                
    # filter top 10 users for the final result          
    with open('top_users.txt','w') as users:
        for i in range(10):
            final_leader_board[i][2] = str(final_leader_board[i][2]) + '\n'
            el=":".join(final_leader_board[i])
            users.write(el)
    
    
    #window for the show top ten gamers
    top_users_window = Toplevel()
    top_users_window.config(bg='black')
    top_users_window.geometry('260x370')
    top_users_window.title('Top_Gamers')

    
    # loop for show User name, amount count and correct answers
    for i in final_leader_board:
        user_info = f"{i[0]} : {i[1]} : {i[2]}"
        label = Label(top_users_window, text=user_info, bg='black', fg='white',font=('arial',12,'bold'))
        label.pack()

    
    

root = create_window()
(
    topframe,
    centerframe,
    rightframe,
    bottomframe,
) = create_positions(root)
put_images_and_buttons(topframe, centerframe, rightframe, bottomframe)
places_questions_and_answers(bottomframe)
root.mainloop()
