from typing import AsyncGenerator


class Coder(object):
    def __init__(self,name,div,age,dob,languages,school,level):
        self.name=name
        self.div=div
        self.age=age 
        self.dob=dob 
        self.languages=languages 
        self.school=school
        self.level=level

    def getLanguage(self):
        return self.languages

    def setLanguage(self,language):
        self.languages=language

    def getAbout(self):
        print(self.name+' '+self.div+' '+self.age+' '+self.dob+' '+self.languages+' '+self.school+' '+self.level)


coder1=Coder("Coder_Name","Class","Age","D.O.B","python,javascript etc.","School Name","His/Her Level")
coder2=Coder("Coder2","Coder2_grade","Age","D.O.B ","JavaScript,react-native,python,c++,css,html","School_Name","Proffesional Coder")


coder1.getAbout()
coder2.getAbout()

print(coder1.getLanguage())
print(coder2.getLanguage())
