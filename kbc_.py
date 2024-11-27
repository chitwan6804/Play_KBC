import time
import win32com.client as wincl
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fifty_fifty(correct_option):
    options=['A','B','C','D']
    options.remove(correct_option)
    incorrect_option= random.choice(options)
    remaining_options=[correct_option,incorrect_option]
    return remaining_options

questions = [
    [
        "What is the capital city of India?",
         "A) Mumbai",
         "B) Kolkata",
         "C) New Delhi",
         "D) Chennai",
         "C"
    ],
    [
        "Which planet is known as the 'Red Planet'?", 
        "A) Venus", 
        "B) Mars", 
        "C) Jupiter", 
        "D) Saturn", 
        "B"
    ],
    [
        "Which of the following is a renewable source of energy?",
        "A) Coal",
        "   B) Natural Gas",
        "C) Solar",
        "D) Nuclear",
        "C"
    ],
    [
        "What is the largest ocean on Earth?",
        "A) Atlantic Ocean",
        "B) Indian Ocean",
        "C) Southern Ocean",
        "D) Pacific Ocean",
        "D"
    ],
    [
        "Who is known as the Father of the Nation in India?",
        "A) Jawaharlal Nehru",
        "B) Sardar Vallabhbhai Patel",
        "C) Mahatma Gandhi",
        "D) Subhas Chandra Bose",
        "C"
    ],
    [
        "What is the chemical symbol for water?",
        "A) O2",
        "B) H2O",
        "C) N2",
        "D) H2SO4",
        "B"
    ],
    [
        "What is the chemical symbol for gold?", 
        "A) Go", 
        "B) Au", 
        "C) Ag", 
        "D) Ge", 
        "B"
    ],
    [
        "Which organ in the human body is responsible for pumping blood?",
        "A) Heart",
        "B) Lungs",
        "C) Liver",
        "D) Kidneys",
        "A"
    ],
    [
        "What is the currency of Japan?",
        "A) Yuan",
        "B) Yen",
        "C) Won",
        "D) Ringgit",
        "B"
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?",
        "A) William Shakespeare",
        "B) Jane Austen",
        "C) Charles Dickens",
        "D) Leo Tolstoy",
        "A"
    ],
    [
        "In which year did Christopher Columbus reach the Americas?",
        "A) 1492",
        "B) 1588",
        "C) 1620",
        "D) 1776",
        "A"
    ],
    [
        "Who wrote the famous play 'Hamlet'?", 
        "A) Charles Dickens", 
        "B) Jane Austen", 
        "C) William Shakespeare", 
        "D) F. Scott Fitzgerald", 
        "C"
    ],
    [
        "What is the largest mammal on Earth?", 
        "A) Elephant", 
        "B) Blue Whale", 
        "C) Giraffe", 
        "D) Polar Bear", 
        "B"
    ],
    [
        "In which year did the Titanic sink?", 
        "A) 1905", 
        "B) 1912", 
        "C) 1920", 
        "D) 1931", 
        "B"
    ],
    [
        "What is the capital city of Australia?", 
        "A) Sydney", 
        "B) Melbourne", 
        "C) Canberra", 
        "D) Brisbane", 
        "C"
    ]
]


levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
speak_level=["1 thousand","2 thousand","3 thousand","5 thousand","10 thousand","20 thousand"
             ,"40 thousand","80 thousand","1 lakh 60 thousand","3 lakh 20 thousand","6 lakh 40 thousand"
             ,"12 lakh 50 thousand","25 lakh","50 lakh","1 Crore"]

i=0
money=0
money_s=0

clear_screen()
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)

spk.Speak("Welcome to Our game KBC!")
clear_screen()
count_= 0
for i in range(0,len(questions)):
    question=questions[i]

    print(f"\n\nQuestion No. {i+1} for Rs{levels[i]} is going to be presented on your screen now!\n")
    spk.Speak(f"Question Number {i+1} for Ruppees{speak_level[i]} is going to be presented on your screen now!")
    
    print(question[0])
    spk.Speak(f" {question[0]}")
    print(f"{question[1]}\t\t{question[2]}")
    print(f"{question[3]}\t\t{question[4]}")
    spk.Speak(f" {question[1]} , {question[2]} , {question[3]} , {question[4]}")
    # spk.Speak(f" {question[1]}")
    # spk.Speak(f" {question[2]}")
    # spk.Speak(f" {question[3]}")
    # spk.Speak(f" {question[4]}")
    spk.Speak("Press 1 for lifeline!")
    print("If You need to take Lifeline: 50-50 then press 1\nNote: You can only use this lifeline twice So use wisely!")
    spk.Speak(f"Your Answer:")
    reply = input("Answer to this question (or type 'quit' to exit): ").strip().upper()

    if reply=="1":
        if(count_<3):
            remaining_options = fifty_fifty(question[-1])
            print("Options:")
            for option in remaining_options:
                if option=='A':
                       option=question[1]
                if option=='B':
                       option=question[2]
                if option=='C':
                       option=question[3] 
                if option=='D':
                       option=question[4]
                print(f"{option}")
                print(f"count means::{count_}")
            count_=count_+1
        else:
            print("Sorry! You have used your lifeline!")
        spk.Speak(f"Your Answer:")
        reply = input("Answer to this question (or type 'quit' to exit): ").strip().upper()

    if reply == 'QUIT':
        print(f"You chose to quit. You won Rs.{money}.")
        spk.Speak(f"You chose to quit. You won Rs.{money_s}.")
        time.sleep(2)
        clear_screen()
        break
    elif reply == question[-1]:
        print(f"Correct answer!\nYou won Rs.{levels[i]} for this level.")
        spk.Speak(f"Correct answer!\nYou won Ruppees {speak_level[i]} for this level.")
        money = levels[i]
        money_s=speak_level[i]
        time.sleep(2)
        clear_screen()
    else:
        if i<5:
            money = 0
            money_s="zero"
        if i >= 5:
            money = 10000
            money_s="10 thousand"
        if i > 9:
            money = 320000
            money_s="3 lakh 20 thousand"
        if i > 14:
            money = 10000000
            money_s="1 Crore"
        print(f"Wrong Answer! You won Rs.{money}.")
        spk.Speak(f"Wrong Answer! You won Ruppee{money_s}.")
        time.sleep(3)
        clear_screen()
        break
time.sleep(2)
print(f"Total Amount::{money}")
spk.Speak(f"Congratulations!\nTotal Amount won by you in this game is ::{money_s} ")

