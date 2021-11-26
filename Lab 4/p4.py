import csv
from functools import reduce
def get_final_grades():
    # Weighting for each of the test
    mark_weight=[0.2,0.25,0.25,0.3]
    with open('grades.csv') as file:
        # Using list comprehension with reduce and lambda to sum up the weighted value if the score of the mark is not -1
        students_grades={line[0]:reduce(lambda x,y:x+y,[float(line[i])*mark_weight[i-1] if float(line[i])!=-1 else 0 for i in range(1,5)])for line in csv.reader(file)}
    return students_grades
