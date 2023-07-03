import json

def load_students():
    with open("students.json", "r") as f:
        '''
        Получает список студентов
        '''
        data = json.load(f)
        return data

def load_professions():
    with open("professions.json", "r") as f:
        '''
        Получает список профессий
        '''
        data = json.load(f)
        return data

def get_students_by_pk(pk):
    '''
    Получает словарь с данными студента
    '''
    student_data = load_students()
    for student in student_data:
        if student["pk"] == pk:
            return student

def get_profession_by_title(title):
    '''
    Получает словарь с информацией о профессии
    '''
    profession_data = load_professions()
    for profession in profession_data:
        if profession["title"] == title:
            return profession

def check_fitness(student, profession):
    '''
    Получает словарь с результатами студента
    '''
    student_skills_set = set(student["skills"])
    profession_skills_set = set(profession["skills"])

    student_has = profession_skills_set.intersection(student_skills_set)
    student_lacks = profession_skills_set.difference(student_skills_set)

    fit_percent = len(student_has) / len(profession_skills_set) * 100

    return {
        "has": list(student_has),
        "lacks": list(student_lacks),
        "fit_percent": int(fit_percent)
    }






