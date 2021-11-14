def get_final_grades(filename='grades.csv'):
    students_grades={}
    with open('grades.csv') as file:
        for line in file:
            mark=0
            result=line.replace('\n','').split(',')
            for i in range(1,5):
                mark+=0 if result[i]=='-1' else float(result[i])*(0.2 if i==1 else 0.25 if i==2 or i==3 else 0.3 )
            students_grades[result[0]]=mark
    return students_grades
