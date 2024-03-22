import json


def calculate_accuracy(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    total_questions = len(data['answers'])
    correct_answers = 0

    for question in data['answers']:
        user_answer = question['answer']
        correct_answer = question['correct']
        if user_answer == correct_answer:
            correct_answers += 1

    accuracy_percentage = (correct_answers / total_questions) * 100
    return accuracy_percentage


accuracy = calculate_accuracy("C:/Users/admin/Downloads/answers (3).json")
print(f"Accuracy: {accuracy:.2f}%")


