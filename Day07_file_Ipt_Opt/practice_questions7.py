#create a file "practice.txt" using python add some sentence

with open("practice.txt","w") as f:
    f.write("hi everyone \nwe are learning fileI\O\n")
    f.write("using java \nI like programing in java")
    
#WAF that replace all occurence of 'java' with 'python' in above file

with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)

#search if the word "learning" exists in the file or not

word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("FOUND")
    else:
        print("not found") 

#WAF to find in which line of the file does the word "learning" occur first print -1 if word is not found

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
        return -1
print(check_for_line())

#from a file containing numbers seprated by comma,print the count of even number (1,2,76,84,90,101)

with open("demo.txt","r") as f:
    data=f.read()
    print(data)
nums=""
for i in range(len(data)):
    if(data[i]==","):
        print(int(nums))
        nums=""
    else:
        nums+=data[i]
         


