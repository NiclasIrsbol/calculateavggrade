import sys
import ast

def main(grades, ects):
    total_ects = 0
    total_points = 0
    grades = ast.literal_eval(sys.argv[1])
    ects = ast.literal_eval(sys.argv[2])
    if len(grades) != len(ects):
        raise Exception("Lists not of equal length")

    for i in range(len(grades)):
        for j in range(len(ects)):
            if i == j:
                total_ects += ects[j]
                total_points += grades[i] * ects[j]

    if total_ects == 0:
        raise Exception("Cannot divide by zero")

    return total_points / total_ects

avg = main(None, None)
print(avg)
