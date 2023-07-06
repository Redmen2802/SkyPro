import json

from question import Question


def load_questions(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item["q"]
        difficulty = int(item["d"])
        right_answer = item["a"]
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions

def build_statistics(questions):
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count + 1
    return f"Вот и всё! " \
           f"Отвечено {count} вопроса из 10 \n" \
           f"Набрано баллов: {score}"
