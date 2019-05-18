responses =["Welcome to my page","My name is abhi","Thank you to visit my page","Sorry, this is beyondmy ability","I am good","Abhishek singh"]

def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    L= a if a<b else b
    while L>=1:
        if a%L==0 and b%L==0:
            return L
        L-=1

def add(a,b):
    return a+b
def sub(a,b):
    return(a-b)
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def how():
    print(response[4])
def create():
    print(response[5])

operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,
            "SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,"MULTIPLY":multiply,
            "product":multiply,"MULTIPLICATION":multiply,"DIVIDE":division,
            "DIVISION":division,"HCF":hcf,"LCM":lcm }
operations1={"+":add,"-":sub,"*":multiply,"/":division}
commands={"NAME":myname,"HOW":how,"END":end,"EXIT":end,"CLOSE":end,"BYE":end,"CREATE":create,"OWNER":create}

