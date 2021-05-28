#Python


                                                            Get started to python...


=>What is python ?


You can't say that Python is written in some programming language, since Python as a language is just a set of rules (like syntax rules, or descriptions of standard functionality).
So we might say, that it is written in English :).  However, mentioned rules can be implemented in some programming language.
Hence, if you send a string like 'import this' to that program called interpreter, it'd return you "Zen of Python".
Since most modern OS are written in C, compilers/interpreters for modern high-level languages are also written in C. 
Python is not an exception - its most popular/"traditional" implementation is called CPython and is written in C.

There are other implementations:





[IronPython](http://ironpython.codeplex.com/) (Python running on .NET)


[Jython](http://www.jython.org/) (Python running on the Java Virtual Machine)


[PyPy](http://pypy.org/) (A fast python implementation with a JIT compiler)


[Stackless](http://www.stackless.com/) Python (Branch of CPython supporting microthreads)


** Python is object orientation programming interpreter language used to code programmes and language is english for coding . **




=>How to create your own python files of classes for object in PYTHON ?

class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())

**FOR BETTER DEMONSTRATION SEE Python File myClasses.py**



=>How to create functions in python ?

def foo(bar):
    """
    Takes bar and does some things to it.
    """
    return bar

help(foo)
foo(bar)
    Takes bar and does
    some things to it

** You can create your own one using def command **


=>What is ' HOWDOI '?

usage: howdoi [-h] [-p POS] [-n NUM] [-a] [-l] [-c] [-x] [-C] [-j] [-v] [-e [ENGINE]] [--save] [--view] [--remove]
              [--empty]
              [QUERY [QUERY ...]]

instant coding answers via the command line

positional arguments:
  QUERY                 the question to answer

optional arguments:
  -h, --help            show this help message and exit
  -p POS, --pos POS     select answer in specified position (default: 1)
  -n NUM, --num NUM     number of answers to return (default: 1)
  -a, --all             display the full text of the answer
  -l, --link            display only the answer link
  -c, --color           enable colorized output
  -x, --explain         explain how answer was chosen
  -C, --clear-cache     clear the cache
  -j, --json            return answers in raw json format
  -v, --version         displays the current version of howdoi
  -e [ENGINE], --engine [ENGINE]
                        search engine for this query (google, bing, duckduckgo)
  --save, --stash       stash a howdoi answer
  --view                view your stash
  --remove              remove an entry in your stash
  --empty               empty your stash

environment variable examples:
  HOWDOI_COLORIZE=1
  HOWDOI_DISABLE_CACHE=1
  HOWDOI_DISABLE_SSL=1
  HOWDOI_SEARCH_ENGINE=google
  HOWDOI_URL=serverfault.com

** A type of search engine ( like google ) runs on command prompt by command lines to learn about python & their usage in simple words to query about PYTHON language **

=>What is ' PIP ' ?

Python's package installer like in javascript it's libraries which let you write easy codes for games like text , velocity etc.
 and in react native it's dependencies which helps in creation of apps by just a command for e.g <Text> , <Image> etc. but in python
it is known as modules or python modules which helps in creation of your programme . So pip is python package manager which let you to
install python packages . ' howdoi ' is also one of it .

=>How to use forloop in python ?

mylist = [1,2,3]
for item in mylist:
    print item

mydict  = {1:'one', 2:'two', 3:'three'}
for key in mydict:
    print key, mydict[key]

**By this you can loop any thing in python**

=>How to Create if condition in python ?

if (cond1 == 'val1' and cond2 == 'val2' and
       cond3 == 'val3' and cond4 == 'val4'):
    do_something

** You can write condition by this **

=>How to use ' while loop ' in python ?

while True:
  stuff()
  if fail_condition:
    break

** To loop anything in fix condition **











 ------------------------------------------------------------------- x -----------------------------------------------------------


                                                     THANK YOU FOR READING ......




Document by : Satvik 

Document On Language : Python

Source : python package ' howdoi ' & other .









