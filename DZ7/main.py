'''
Импорт функций
'''
from utils import get_students_by_pk, get_profession_by_title, check_fitness

def main():

    students_pk = input("Введите номер студента: ")

    if students_pk.isdigit():
        student = get_students_by_pk(int(students_pk))

        if student:
            print(f"Студент {student['full_name']}\n"
                  f"знает {', '.join(student['skills'])}")
            profession_title = input("Введите название профессии: ").title()
            profession = get_profession_by_title(profession_title)

            if profession:
                fitness = check_fitness(student, profession)
                print(f"Пригодность {fitness['fit_percent']}%\n"
                      f"{student['full_name']} знает: {', '.join(fitness['has'])}\n"
                      f"{student['full_name']} не знает: {', '.join(fitness['lacks'])}")
            else:
                print("У нас нет такой специальности!")
                return
        else:
            print("У нас нет такого студента")
            return
    else:
        print("Вы ввели не число!")

if __name__ == '__main__':
    main()