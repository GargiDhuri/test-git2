import os
from pypdf import PdfWriter
#os.mkdir('D:\Pyt')
os.chdir('D:\Pyt')
dirloc=os.getcwd()
'''for i in range (1,10):
    with open("{}hello_world.txt".format(i), "w") as f:
        pass
frmt=input("Enter the required format")
cnt=1
for file in os.listdir(dirloc):
    if file.endswith(frmt):
        os.rename(file,f"{cnt}.{frmt}")
        cnt+=1
'''
list1=[]
for file in os.listdir(dirloc):
    while len(list1)<3:
        if file.endswith('.pdf'):
            list1.append(file)
    
merger = PdfWriter()

for pdf in list1:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
