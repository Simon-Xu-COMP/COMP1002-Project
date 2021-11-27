"""
The model 
    includes user information being represented, and will be acted upon latter. 
    determine the system state
"""
from os import error
import sys
from collections import defaultdict

class Model:

    NUM_FILES = 7
    
    def _init_(self):
        self.info = []   # [user id, last name, first name, department, number of injection,[injection info],'studentornot']
        self.pass_info = [] # [user id, password]

        self.id = defaultdict(list)
        self.nme = defaultdict(list)
        self.dpt = defaultdict(list)
        self.isInjected = defaultdict(list)
        self.isStu = defaultdict(list)
        self.userIndex = defaultdict(list)
        self.password = dict()
    
    @property
    def info(self):
        return self.info
    """
    getter of info.
    Use it by 
    c = Model()
    c.info
    """
    
    @property
    def password(self):
        return self.password
    """
    getter of password
    use it by
    c = Model()
    c.password
    """
    
    def create_new(self):
        print("Create new file")
        FL = open("storage.txt","x")
        FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
        FL.close()
        """
        Transfer data into the system and writes the specified string to a file. 
        The string content is stored in the buffer until the file is closed or the buffer is flushed
        
        Returns:
        None
        """
    
    
    def wrong_file(self):
        s = input("Unexcepted information in storage file, create a new file? [y/n]")
        if(s == 'y' or s == 'Y'):
            self.info.clear()
            FL = open("storage.txt","w")
            FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
            FL.close()
            self.init()
        else:
            print('Program Exit')
            sys.exit()
        """
        When an error occurs in the read data, a new file is generated.
        
        Returns:
        None
        """

    def load_file(self):
        try:
            FL = open("storage.txt","r", encoding = 'UTF-8')
        except FileNotFoundError:
            self.create_new()
            FL = open("storage.txt","r", encoding = 'UTF-8')
        for i in FL.readlines():
            try:
                eval(i)
            except Exception:
                FL.close()
                self.wrong_file()
                break
            if isinstance(eval(i), list) == 0:
                FL.close()
                self.wrong_file()
                break
            if(len(eval(i)) != Model.NUM_FILES):
                FL.close()
                self.wrong_file()
                break
            for j in enumerate(i):
                if isinstance(j[1],str) == 1:
                    i[j[0]] = j[1].lower()
            self.info.append(eval(i))
        FL.close()
        """
        Open the TXT document and call create_new() if encounter a IOE error
        Try evall the stored personnel information and call wrong_file () if error occurs
        Check if it is a known type list and call wrong_file () if is not list
        When the length of info is not 7, the wrong_file() is invoked if the length is illegal
        
        
        Returns:
        None
    
        Raises:
        Exception: An error occurred accessing the text.
        """

    def read_password(self):
        FL = open("password.txt", "r", encoding = "UTF-8")
        for i in FL.readlines():
            self.pass_info.append(eval(i))
    
    
    def update_password(self, id, new):
        self.password[id] = new
        self.pass_info[self.userIndex[id][1]][1] = new
    
    
    def init(self):
        self.load_file()
        self.read_password()
        for j in enumerate(self.info[1:]):
            i = j[1]
            id[i[0]].append(i)
            self.nme[i[1] + i[2]].append(i)
            self.dpt[i[3]].append(i)
            self.isInjected[i[4]].append(i)
            self.isStu[i[6]].append(i)
            
            self.userIndex[i[0]].append(j[0])
        for j in enumerate(self.pass_info):
            i = j[1]
            self.password[i[0]] = i[1]
            self.userIndex[i[0]].append(j[0])
        """
        Initialize the file and write the contents to the list
        """
    
    
    def write_file(self):
        FL = open("storage.txt", "w")
        for i in self.info:
            FL.write('[')
            for j in i:
                if isinstance(j, list):
                    FL.write('[')
                    for k in j:
                        FL.write("'" + str(k) + "'" + ',')
                    FL.write('],')
                else:
                    FL.write("'" + str(j) + "'" + ',')
            FL.write(']\n')
        FL.close()
        FL = open("password.txt", "w")
        for i in self.pass_info:
            FL.write('[')
            for j in i:
                FL.write("'" + str(j) + "'" + ',')
            FL.write(']\n')
        FL.close()
        """
        Store the read content in the middle of memory, write according to the format
        """
    
