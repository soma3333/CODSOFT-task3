import random
capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit=['1','2','3','4','5','6','7','8','9','0']
special=['~','!','@','#','$','%','^','&','*']

length=int(input("Enter the length of password required: "))
print("COMPLEXITY LEVEL:")
print("Press 1 to include only capital and small letter alphabets")
print("Press 2  to include  Digits also")
print("Press 3 to include Special characters also")
print("")
user=int(input("Enter the password complexity no : "))
c=[]
if user==1:
    b=random.choices(capital)+random.choices(small)
    a=capital+small
    for i in range(length-2):
         random.shuffle(a)
         b=b+random.choices(a)
elif user==2:
    b=random.choices(capital)+random.choices(small)+random.choices(digit)
    a=capital+small+digit
    for i in range(length-3):
         random.shuffle(a)
         b=b+random.choices(a)
elif user==3:
    b=random.choices(capital)+random.choices(small)+random.choices(digit)+random.choices(special)
    a=capital+small+digit+special
    for i in range(length-4):
         random.shuffle(a)
         b=b+random.choices(a)
else:
    print("Enter correct complexity no....")


s=""
random.shuffle(b)
for i in b:
    s=s+i
print("")
print("Generated password is : ",s)    

