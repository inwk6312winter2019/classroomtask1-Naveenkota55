#lab 4 task1
'''import string
def string1():
    file1 = open("words.txt","r")
    punct = string.punctuation
    for a in file1:
        a = a.strip()
        a = a.replace(" ","")
        for c in punct:
           a = a.replace(c,"")
        a = a.lower()
        print(a)

string1()'''

#lab 4 task 2
'''
import string
def stringoperation():
    myfile = open("file1.txt","r")
    punct = string.punctuation
    for my in myfile:
        my = my.strip()
        my = my.replace(" ","\n")
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        print(my)
stringoperation()
'''

#LAB4 TASK2_2
'''
import string
def string1():
    file_1 = open("file1.txt","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    for my in file_1:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    print("Words usage:",histo)
    print("Total no of words:",len(listofwords))

string1()
'''
#lab 4 task 3

'''
import string
def string1():
    myfile = open("FIfile1","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    for my in myfile:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    for key, value in histo.items():
        if(value == 20):
            print(key)

string1()


'''
#lab 4 task 7
'''
import string
def removepattern(word):
    punc = string.punctuation
    stri = ""
    for p in punc:
        stri = word.strip()
        stri = word.replace(p,'')

    return stri

def sfunc1(filename1,filename2):
     try:
        master = open(filename1,"r")
        slave = open(filename2,"w")
        for ma in master:
            new = removepattern(ma)
            slave.write(ma)

        print("File write operation completed successfully :-)")
     except:
        print("Oops something went wrong!!!")


x = input("Enter master file for copy operation:")
y = input("Enter slave file:")
sfunc1(x,y)
'''
#lab4 task6
'''
import os
def walk(dirname):    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)        
        if os.path.isfile(path):
            print(path)        
        else:            
            walk(path)

walk(os.getcwd())'''





