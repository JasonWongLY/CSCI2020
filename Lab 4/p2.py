import argparse,re
parser=argparse.ArgumentParser()
parser.add_argument("input_filename","output_filename")
#parser.add_argument()
args=parser.parse_args()
print(args.input_filename)
print(args.output_filename)
question_mark="?"
star_mark="*"
'''if re.search(question_mark,filename)or re.search(star_mark,filename):
    try:
        f=open(filename,"r")
    except IOError:
        print("No matching")
else:
    try:
        f=open(filename,"r")
        output="Number of characters: "+"Number of words: "+"Number of lines: "+"Number of digits: "

    except IOError:
        print("Opening file " + filename + "failed")'''
def count(filename):
    line_count=0
    word_count=0
    character_count=0
    digit_count=0
    with open(filename) as file:
        text=file.read()
        character_count=len(text)
        for char in text:
            if char.isdigit():
                digit_count+=1
        for line in file:
            line_count+=1
            word_count+=len(line.split())

    return (character_count,word_count,line_count,digit_count)
