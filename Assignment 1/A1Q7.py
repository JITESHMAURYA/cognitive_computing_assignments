file=open("assignment1_question7.txt","w")

file.write("Jitesh Maurya\n")
print("Data written in file")
file.close()

file=open("assignment1_question7.txt","r")
print(file.read())
file.close()

file=open("assignment1_question7.txt","a")
file.write("Jitesh Maurya the great\n")
file.close()

file=open("assignment1_question7.txt","r")
print(file.read())
file.close()

file=open("assignment1_question7.txt","r")
print('Number of lines:',len(file.readlines()))
file.close()