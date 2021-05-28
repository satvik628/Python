from typing import AsyncGenerator


# Creating self-made class
class Coder(object):
    def __init__(self,name,div,age,dob,languages,school,level):
        self.name=name
        self.div=div
        self.age=age 
        self.dob=dob 
        self.languages=languages 
        self.school=school
        self.level=level

# Function to get languages
    def getLanguage(self):
        return self.languages

    def setLanguage(self,language):
        self.languages=language
        

# Function to get all details about asked ( See line 27 , 28 , 31 & 32 )
    def getAbout(self):
        print(self.name+' '+self.div+' '+self.age+' '+self.dob+' '+self.languages+' '+self.school+' '+self.level)
        

# Using ' Coder ' class to store details 
# Creating variable to store details 

coder1=Coder("Coder_Name","Class","Age","D.O.B","python,javascript etc.","School Name","His/Her Level")
coder2=Coder("Coder2","Coder2_grade","Age","D.O.B ","JavaScript,react-native,python,c++,css,html","School_Name","Proffesional Coder")


# Using getAbout() function to get details of variable coder1 & coder2
coder1.getAbout()
coder2.getAbout()

# Using getLanguage() function to get coder1's & coder2's languages 

print(coder1.getLanguage())
print(coder2.getLanguage())

