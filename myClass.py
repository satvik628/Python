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


satvik=Coder("Satvik","8A","13","6-Feb-2008","Javascript,react-native,css,html,python","The lovedale sr. sec. school satna(MP)","Proffesoner")
teacher=Coder("Swetha Mam","Learnt","NA","9 JAN ","JavaScript,react-native,python,c++,css,html","Whitehat JR.","Proffesional Coder")

satvik.getAbout()
teacher.getAbout()