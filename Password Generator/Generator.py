import random
file=open('pwd.txt',"a")
char = "aBcDeFgHiJkLmNoPqRsTuVwXyZ!@#$1234567890"
y="y"
Y="Y"

def gp(x):
    pwd = "".join(random.sample(char, x))
    return pwd

nam=input(" Provide a name for password:\n\t--> ")
len=input("\n Length of password:\n\t--> ")
length=int(len)
while True:
    input("\n\tPress Enter to generate new password")
    gpp=gp(length)
    print("\n\t"+gpp)
    inp=input("\n Is it perfect? [y/n] <You can also press enter for no>\n\t-->")
    if inp==y or inp==Y:
        file.write("    "+nam+"::: "+gpp+'\n\n')
        file.close()
        print(f"\n\t\tDone! Saved password '{gpp}' for {nam}.\n\n")
        exit=input(" Press enter to exit.")
        break
    else:
        continue
