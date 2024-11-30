if __name__ == '__main__':
    n = int(input())
    students = []

    for i in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    s = set([grade for name, grade in students])
    grades = sorted(s)
    second_lowest_grade = grades[1]

    names = []
    for name, grade in students:
        if grade == second_lowest_grade:
            names.append(name)

    names.sort()
    for name in names:
        print(name)
