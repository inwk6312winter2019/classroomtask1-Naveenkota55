import string
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

string1()
