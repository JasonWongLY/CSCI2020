import argparse,re,os,glob

# initilize
question_mark="?"
star_mark="*"
path=os.getcwd()

# get input from command line
parser=argparse.ArgumentParser()
parser.add_argument('input',type=str,nargs='+')
args=parser.parse_args() # args.input[0] = input.txt
input_filename=args.input[0]
output_filename=args.input[1]

def count(filename):
    line_count=0
    word_count=0
    character_count=0
    digit_count=0
    with open(str(filename),'r') as file:
        for line in file:
            line_count+=1
            word_count+=len(line.split())
            for char in line:
                if char.isalpha():
                    character_count+=1
                if char.isdigit():
                    digit_count+=1

    return (character_count,word_count,line_count,digit_count)


if input_filename.find(question_mark)!=-1 or input_filename.find(star_mark)!=-1:

    f=glob.iglob(args.input[0])
    for searched_file in f:
        #with open(str(searched_file),'r') as open_file:
        ans=count(searched_file)
        try:
            w = open(output_filename, 'a')
            w.write("Name of file: "+searched_file+ "\nNumber of characters: " + str(ans[0]) + "\nNumber of words: " + str(ans[1]) + "\nNumber of lines: " + str(ans[2]) + "\nNumber of digits: " + str(ans[3])+"\n")
        except IOError:
            print("Opening file " + output_filename + "failed")


else:
    try:
        f=open(input_filename,"r")
        ans=count(input_filename)
        try:
            w = open(output_filename, 'w')
            w.write("Number of characters: " + str(ans[0]) + "\nNumber of words: " + str(ans[1]) + "\nNumber of lines: " + str(ans[2]) + "\nNumber of digits: " + str(ans[3]))
        except IOerror:
            print("Opening file " + output_filename + "failed")


    except IOError:
        print("Opening file " + input_filename + "failed")

