def UpDown(i,x):
    if (x=='U'):
        if (i==0):
            return i
        else:
            return i-1
    else:
        if (i==2):
            return i
        else:
            return i+1
def RightLeft(j,x):
    if (x=='L'):
        if (j==0):
            return j
        else: 
            return j-1
    else:
        if (j==2): 
            return j
        else: 
            return j+1
key=[[1,2,3],[4,5,6],[7,8,9]]
j=1
i=1
print("Your keypad:")
for z in key:
    print('  '.join(map(str, z)))
file1= r"C:\Users\E14\Desktop\Psswrd\doc.txt" #put file location
print("Your password is:")
with open(file1,'r') as f:
    for line in f:
        for char in line:
            if (char=='U' or char=='D'):
                i=UpDown(i,char)
            elif (char=='R' or char=='L'):
                j=RightLeft(j,char)
        print(key[i][j],end="")
