import tkinter as tk
from tkinter import messagebox

# Define the quiz data
cs_quiz = {
    "1. What is the primary characteristic of Python programming language?": {
        "options": ["A) Compiled", "B) Interpreted", "C) Hybrid", "D) Scripted"],
        "answer": "B"
    },
    "2. Which data structure uses FIFO (First-In-First-Out) principle?": {
        "options": ["A) Stack", "B) Tree", "C) Queue", "D) Graph"],
        "answer": "C"
    },
    "3. What does 'HTTP' stand for?": {
        "options": [
            "A) Hyper Text Transfer Protocol",
            "B) High Traffic Text Process",
            "C) Home Tool Transfer Package",
            "D) Hyperlink Translation Type Protocol"
        ],
        "answer": "A"
    },
    "4. Which algorithm is used for searching in a sorted array efficiently?": {
        "options": ["A) Bubble Sort", "B) Binary Search", "C) Linear Search", "D) Quick Sort"],
        "answer": "B"
    },
    "5. What is the time complexity of a binary search algorithm?": {
        "options": ["A) O(n)", "B) O(log n)", "C) O(n²)", "D) O(1)"],
        "answer": "B"
    },
    "6. Which of these is NOT a programming paradigm?": {
        "options": ["A) Object-Oriented", "B) Functional", "C) Modular", "D) Fractional"],
        "answer": "D"
    },
    "7. What does SQL stand for?": {
        "options": [
            "A) Structured Question Language",
            "B) Standard Query Language",
            "C) Structured Query Language",
            "D) System Query Logic"
        ],
        "answer": "C"
    },
    "8. Which protocol is used for secure communication over a network?": {
        "options": ["A) HTTP", "B) FTP", "C) HTTPS", "D) SMTP"],
        "answer": "C"
    },
    "9. What is the main purpose of an operating system?": {
        "options": [
            "A) Run applications",
            "B) Manage hardware resources",
            "C) Design websites",
            "D) Create documents"
        ],
        "answer": "B"
    },
    "10. Which data type represents true/false values in Python?": {
        "options": ["A) bool", "B) int", "C) float", "D) str"],
        "answer": "A"
    }
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Programming Quiz")
        
        self.current_question = 0
        self.score = 0
        self.questions = list(cs_quiz.keys())
        
        self.create_widgets()
        self.load_question()
    
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)
        
        self.var = tk.StringVar()
        
        self.option1 = tk.Radiobutton(self.root, text="", variable=self.var, value="A", font=("Arial", 12))
        self.option1.pack(anchor="w")
        
        self.option2 = tk.Radiobutton(self.root, text="", variable=self.var, value="B", font=("Arial", 12))
        self.option2.pack(anchor="w")
        
        self.option3 = tk.Radiobutton(self.root, text="", variable=self.var, value="C", font=("Arial", 12))
        self.option3.pack(anchor="w")
        
        self.option4 = tk.Radiobutton(self.root, text="", variable=self.var, value="D", font=("Arial", 12))
        self.option4.pack(anchor="w")
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=20)
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            options = cs_quiz[question]["options"]
            
            self.question_label.config(text=question)
            self.option1.config(text=options[0])
            self.option2.config(text=options[1])
            self.option3.config(text=options[2])
            self.option4.config(text=options[3])
            
            self.var.set(None)  # Clear previous selection
        else:
            self.show_results()
    
    def check_answer(self):
        question = self.questions[self.current_question]
        correct_answer = cs_quiz[question]["answer"]
        
        if self.var.get() == correct_answer:
            self.score += 1
        
        self.current_question += 1
        self.load_question()
    
    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(cs_quiz)}")
        self.root.quit()

# Create the main window
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()
