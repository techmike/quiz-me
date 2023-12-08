import json
import random

def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def quiz_user(questions):
    score = 0
    total_questions = len(questions)
    answered_questions = 0

    question_ids = list(questions.keys())
    random.shuffle(question_ids)

    for q_id in question_ids:
        question_data = questions[q_id]
        question = question_data['question']
        answer = question_data['answer']
        options = question_data['incorrect'] + [answer]
        random.shuffle(options)

        print(question)
        print("Options:")
        for idx, option in enumerate(options):
            print(f"{idx + 1}. {option}")

        user_input = input("Your answer (enter the option number or 'exit' to end the quiz): ")

        if user_input.lower() == 'exit':
            print("Exiting the quiz...")
            break

        try:
            user_choice = int(user_input) - 1
            user_answer = options[user_choice]
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {answer}")
            answered_questions += 1
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")

    print("Quiz Complete!")
    if answered_questions > 0:
        print(f"You answered {answered_questions} out of {total_questions} questions.")
        print(f"You scored {score}/{answered_questions}.")

if __name__ == "__main__":
    file_path = "crest-cpsa-exam.json"  # Replace with your JSON file path
    questions = load_questions_from_json(file_path)
    quiz_user(questions)

