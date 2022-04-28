'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def pro(a):
    temp=a
    b=[]
    
    for i in range(len(a)):
        if i+1 != len(a):
            if a[i]==a[i+1]:
                b.append(a[i])
    if len(b)==0:
        print(temp)
        exit()
    else:
        q=a.replace(b[0], "")
        temp=q
        pro(q)
                
    #print(temp)
a="cherreis"
pro(a)

