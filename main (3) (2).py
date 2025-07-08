import tkinter as tk
from tkinter import messagebox
import random

# -------------- questions data --------------
questions_data = {
    "History": [
        {"question": "Who was the first president of the USA?", "options": ["Lincoln", "Washington", "Jefferson", "Adams"], "answer": "Washington"},
        {"question": "In what year did World War II end?", "options": ["1945", "1939", "1940", "1950"], "answer": "1945"},
        {"question": "Where was Napoleon from?", "options": ["Spain", "France", "Italy", "Germany"], "answer": "France"},
        {"question": "Who discovered America?", "options": ["Columbus", "Magellan", "Cook", "Vasco da Gama"], "answer": "Columbus"},
        {"question": "Which wall fell in 1989?", "options": ["China Wall", "Berlin Wall", "Paris Wall", "London Wall"], "answer": "Berlin Wall"},
        {"question": "When was the UN founded?", "options": ["1945", "1919", "1930", "1955"], "answer": "1945"},
        {"question": "Who was Cleopatra?", "options": ["Queen of Egypt", "Queen of Rome", "Greek Princess", "French Queen"], "answer": "Queen of Egypt"},
        {"question": "What empire did Julius Caesar belong to?", "options": ["Roman", "Greek", "Ottoman", "British"], "answer": "Roman"},
        {"question": "Where did the Renaissance start?", "options": ["Italy", "France", "England", "Germany"], "answer": "Italy"},
        {"question": "Who was the first man on the moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "answer": "Neil Armstrong"},
    ],
    "Science": [
        {"question": "What planet is known as the Red Planet?", "options": ["Mars", "Earth", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What gas do plants absorb?", "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen", "Acid"], "answer": "Water"},
        {"question": "How many legs does an insect have?", "options": ["6", "8", "4", "10"], "answer": "6"},
        {"question": "What part of the plant conducts photosynthesis?", "options": ["Leaves", "Roots", "Stem", "Flower"], "answer": "Leaves"},
        {"question": "Which vitamin comes from sunlight?", "options": ["D", "A", "C", "B"], "answer": "D"},
        {"question": "Which blood type is universal donor?", "options": ["O-", "A+", "B-", "AB+"], "answer": "O-"},
        {"question": "What do bees collect?", "options": ["Pollen", "Dust", "Dew", "Seeds"], "answer": "Pollen"},
        {"question": "Which metal is liquid at room temp?", "options": ["Mercury", "Gold", "Iron", "Silver"], "answer": "Mercury"},
        {"question": "What organ pumps blood?", "options": ["Heart", "Lung", "Brain", "Liver"], "answer": "Heart"},
    ],
    "Sports": [
        {"question": "How many players in a football team?", "options": ["11", "9", "10", "12"], "answer": "11"},
        {"question": "Where were the 2020 Olympics held?", "options": ["Tokyo", "London", "Paris", "Beijing"], "answer": "Tokyo"},
        {"question": "What sport uses a shuttlecock?", "options": ["Badminton", "Tennis", "Cricket", "Golf"], "answer": "Badminton"},
        {"question": "Which country won the 2022 World Cup?", "options": ["Argentina", "France", "Brazil", "Germany"], "answer": "Argentina"},
        {"question": "How many rings in the Olympic symbol?", "options": ["5", "4", "6", "7"], "answer": "5"},
        {"question": "What sport is Serena Williams known for?", "options": ["Tennis", "Golf", "Swimming", "Football"], "answer": "Tennis"},
        {"question": "What is the national sport of Japan?", "options": ["Sumo", "Karate", "Judo", "Kendo"], "answer": "Sumo"},
        {"question": "What ball is used in golf?", "options": ["White small", "Big orange", "Black heavy", "Red flat"], "answer": "White small"},
        {"question": "Where is Wimbledon played?", "options": ["London", "Paris", "New York", "Tokyo"], "answer": "London"},
        {"question": "How long is a marathon?", "options": ["42 km", "21 km", "30 km", "50 km"], "answer": "42 km"},
    ],
    "Geography": [
        {"question": "What is the capital of Canada?", "options": ["Ottawa", "Toronto", "Vancouver", "Montreal"], "answer": "Ottawa"},
        {"question": "Which continent is Egypt in?", "options": ["Africa", "Asia", "Europe", "America"], "answer": "Africa"},
        {"question": "Which ocean is the biggest?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "answer": "Pacific"},
        {"question": "What river runs through Egypt?", "options": ["Nile", "Amazon", "Mississippi", "Yangtze"], "answer": "Nile"},
        {"question": "Where is Mount Everest?", "options": ["Nepal", "India", "China", "Pakistan"], "answer": "Nepal"},
        {"question": "What is the smallest continent?", "options": ["Australia", "Europe", "Antarctica", "Asia"], "answer": "Australia"},
        {"question": "Where is the Sahara Desert?", "options": ["Africa", "Asia", "Australia", "America"], "answer": "Africa"},
        {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "Which country has the most people?", "options": ["China", "India", "USA", "Russia"], "answer": "China"},
        {"question": "Which country has pyramids?", "options": ["Egypt", "Mexico", "Peru", "India"], "answer": "Egypt"},
    ]
}

window = tk.Tk()
window.title("Quiz Game")
window.geometry("700x500")
window.config(bg="#f0f0f0")

score = 0
question_index = 0
selected_category = ""

start_frame = tk.Frame(window, bg="#f0f0f0")
title_label = tk.Label(start_frame, text="Quiz Game", font=("Arial", 28, "bold"), bg="#f0f0f0")
name_label = tk.Label(start_frame, text="By: Sewar and Noxy", font=("Arial", 14), bg="#f0f0f0")
title_label.pack(pady=(40, 10))
name_label.pack(pady=(0, 20))
category_label = tk.Label(start_frame, text="Choose a category:", font=("Arial", 16), bg="#f0f0f0")
category_label.pack()

category_buttons = []
def choose_category(cat):
    global selected_category, questions, question_index, score
    selected_category = cat
    questions = questions_data[cat]
    question_index = 0
    score = 0
    start_frame.pack_forget()
    show_question()

for category in questions_data:
    btn = tk.Button(start_frame, text=category, width=20, font=("Arial", 14), bg="#add8e6", command=lambda c=category: choose_category(c))
    btn.pack(pady=5)
    category_buttons.append(btn)

start_frame.pack()

game_frame = tk.Frame(window, bg="#f0f0f0")
question_label = tk.Label(game_frame, text="", wraplength=600, font=("Arial", 16), bg="#f0f0f0")
question_label.pack(pady=20)

option_buttons = []
def check_answer(selected_option):
    global score, question_index
    correct_answer = questions[question_index]["answer"]
    for btn in option_buttons:
        btn.config(state="disabled")
        if btn.cget("text") == correct_answer:
            btn.config(bg="lightgreen")
        elif btn.cget("text") == selected_option:
            btn.config(bg="tomato")
    if selected_option == correct_answer:
        score += 1
    window.after(1000, next_question)

def show_question():
    game_frame.pack()
    for btn in option_buttons:
        btn.destroy()
    option_buttons.clear()

    q = questions[question_index]
    question_label.config(text=f"Q{question_index+1}: {q['question']}")
    for opt in q["options"]:
        btn = tk.Button(game_frame, text=opt, font=("Arial", 12), width=25, height=2, bg="#e0e0e0", command=lambda o=opt: check_answer(o))
        btn.pack(pady=5)
        option_buttons.append(btn)

def next_question():
    global question_index
    question_index += 1
    if question_index < len(questions):
        show_question()
    else:
        show_result()

def show_result():
    game_frame.pack_forget()
    result_frame.pack()
    percent = int((score / len(questions)) * 100)
    result_msg = f"Your Score: {percent}/100"
    if percent == 100:
        result_msg += "\nCongratulations! Perfect Score!"
    result_label.config(text=result_msg)

# ----- Added: Show Answers Function -----
def show_answers():
    answers_text = ""
    for i, q in enumerate(questions):
        answers_text += f"Q{i+1}: {q['question']}\nCorrect Answer: {q['answer']}\n\n"
    messagebox.showinfo("Correct Answers", answers_text)
# ----------------------------------------

result_frame = tk.Frame(window, bg="#f0f0f0")
result_label = tk.Label(result_frame, text="", font=("Arial", 18), bg="#f0f0f0")
result_label.pack(pady=20)

# Play Again Button
restart_btn = tk.Button(result_frame, text="Play Again", font=("Arial", 14), bg="#87cefa", command=lambda: restart_game())
restart_btn.pack(pady=5)

# Show Answers Button (new)
show_answers_btn = tk.Button(result_frame, text="Show Answers", font=("Arial", 14), bg="#ffd700", command=show_answers)
show_answers_btn.pack(pady=5)

def restart_game():
    result_frame.pack_forget()
    start_frame.pack()

window.mainloop()
