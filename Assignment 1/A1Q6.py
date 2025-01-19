x="jitesh maurya"
count=0
for i in x:
    if(i in "aeiouAEIOU"):
        count = count+1
print("number of vowels are :",count)
 
revstring = x[::-1]
print(revstring)

start=0
end=len(x)-1
flag=True
while(start<=end):
    if(x[start] != x[end]):
        flag=False
        break
    start=start+1
    end=end-1
if(flag == False):
    print("the string is not a palindrome!")
else:
    print("the string is a palindrome!")