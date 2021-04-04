n =  input("Enter your name : ")
m = int(input("Enter your marks : "))
p = int(input("Enter your phone number : "))

act  = "Your name is : {}.\nYour marks are : {}.\nYour phone number is : {}."
soc  =  act.format(n,m,p)
print(soc)
with  open ("table.txt" , "a") as f  :
    f.write(soc)
    f.write("\n")
    f.write("***********")
    f.write("\n")
