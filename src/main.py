from os import error
import sys
"""
a list to store the user information, 
user id, last name, first name, department, 
"""
info = []

id = dict()
nme = dict()
dpt = dict()
isInjected = dict()
isStu = dict()

def create_New():
    print("Create new file")
    FL = open("storage.txt","x")
    FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
    FL.close()

def wrongFile():
    s = input("Unexcepted information in storage file, create a new file? [y/n]")
    if(s == 'y' or s == 'Y'):
        FL = open("storage.txt","w")
        FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
        FL.close()
        init()
    else:
        print('Program Exit')
        sys.exit()
        

def load_File():
    try:
        FL = open("storage.txt","r")
    except Exception:
        create_New()
        FL = open("storage.txt","r")
    for i in FL.readlines():
        try:
            eval(i)
        except Exception:
            FL.close()
            wrongFile()
            break
        info.append(eval(i))
    FL.close()

def print_File():
    FL = open("storage.txt","w")
    for i in info:
        FL.write('[')
        for j in i:
            if isinstance(j, list):
                FL.write('[')
                for k in j:
                    FL.write("'"+str(k)+"'"+',')
                FL.write('],')
            else:
                FL.write("'"+str(j)+"'"+',')
        FL.write(']\n')
    FL.close()

def init():
    load_File()
    for i in info[1:]:
        if(len(i) != 7):
            info.clear()
            wrongFile()
            break
        id[i[0]] = i
        nme[i[1]+i[2]] = i
        dpt[i[3]] = i
        isInjected[i[4]] = i
        isStu[i[6]] = i



def main():
    init()
    while True:
        option = str(input("Choose C for using command line interface, choose G for useing graphic user interface"))
        if option == 'G':
            # GUI
            return 0
        elif option == 'C':
            while True:
                # read all info from txt, and store it into storage.
                storage = dict()
                who = str(input("Input u to enter the user login page. Input a to enter the administrator login page. Input b to go back to the last menu."))
                if who == 'u':
                    id = str(input("Please input your user id").split())
                    password = str(input("Please input your password").split())
                    
                    # change password
                    # 
                if who == 'a':
                    
                    
                    break
                if who == 'b':
                    break
        else:
            # try catch needed
            return 0

init()

# f = open("test.txt", "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))
# f.close()

# q = open("test.txt", "a+")
# for i in range(5):
#     q.write("append line %d\r\n" % (i + 1 + 10))
# q.close()

