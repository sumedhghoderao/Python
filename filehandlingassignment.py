# # Q.1)write a program to take some text lines from the user and write it to the file
# with( open('file1.txt',"w") as file):
#     n=int(input("Enter no of lines "))
#     for i in range(0,n): 
#         file.write(input("Enter text"))
#         file.write("\n")

# # Q.2)write a program to read from a file and write to another file
# file1 =open('file1.txt','r')
# file2=open('file2.txt','w')
# file2.write(file1.read())
# file1.close()
# file2.close()

# # Q.3): Write a program to read from a file and modify its content by pre-pending each line with "HPCAP" 
file1=open('file1.txt',"r")
list1=[]
for i in file1:
    list1.append("HPCAP "+i)
    
file1.close()
file1=open("file1.txt","w") 
for j in list1:     
        file1.write(j)
file1.close()
  
  
# # Q.4): Write a program to read from a file, pre-pending each line with "HPCAP" and write to the different file 
        
# file1 =open('file1.txt','r')
# file2=open('file2.txt','w')

# for i in file1:
#     file2.write("HPCAP "+i )
# file1.close()
# file2.close()