## FILE HANDLING

### Introduction to File Handling

# File handling allows Python programs to store, read, and manage data saved on
# the computer -> such as notes, logs, student records, or CSV files.
# Real-world uses:
# • Saving login logs
# • Writing reports
# • Storing student data
# • Reading configuration files
# • Exporting analytics in CSV

### Types of Files

# File Type   ---        Description ---- Example Extensions
# Text Files  ----  Human-readable content ---- . txt, .csv,. log
# Binary Files ----  Data stored in encoded form --- .png, .jpg, .mp4, .pdf,.exe
# Examples:
# • A file named notes.txt storing  Python concepts → text file
# • A file named profile.jpg storing photo → bincdary file


# Write a program to read a text from a given file certificate.txt
# and find whether it contains the word live.
# Syntax:

# file = open("python-basics-revision\File_Handling\certificate.txt","r")
# data = file.read()
# data = data.lower()
# if "live" in data:
#     print("Yes, live word is present in the txt file.")
# else:
#     print("No")
    
# print("File data: ",data)

### Open a file in write mode - (if you open in write mode ,even if file is not created already it will create.)

# file = open("python-basics-revision\File_Handling\ report.txt","w")
# file.write("We can write from here in files very easily.")

### Append mode

# file = open("python-basics-revision\File_Handling\ report.txt","a")
# file.write(" \n We can append data from here in files very easily.")

### x mode (create file and shows error if already exist)

# file = open("python-basics-revision\File_Handling\ report_1.txt","a")
# file.write(" \n We can append data from here in files very easily.")

### with keyword(this help use to automatically close() the file.)

# with open("python-basics-revision/File_Handling/report.txt","r") as f:
#     data = f.read()
#     print("File Data",data)
    
### readlines() - read line by line
# - if data become over in file it will print blank result there.

# with open("python-basics-revision/File_Handling/reading.txt","r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()
#     line4 = f.readline()
#     line5 = f.readline()
#     line6 = f.readline()
#     line7 = f.readline()
#     data = f.read()
#     print("Line1:",line1)
#     print("Line2:",line2)
#     print("Line3:",line3)
#     print("Line4:",line4)
#     print("Line5:",line5)
#     print("Line6:",line6)
#     print("Line6:",line7)
#     print("File data:",data)

### readlines() - read all lines - return list of strings

# with open("python-basics-revision/File_Handling/reading.txt","r") as f:
#     lines = f.readlines()
#     print("All data:", lines)
    
### print how many lines are there in reading.file

# with open("python-basics-revision/File_Handling/reading.txt","r") as f:
#     lines = f.readlines()
#     print("Output of readlines function:", lines)
#     print("No. of lines present in file: ",len(lines))

### Automating file tasks(rename,delete,copy)-> using python modules

#copy file

# import shutil
# shutil.copy('python-basics-revision/File_Handling/ report_1.txt','python-basics-revision/File_Handling/certificate.txt')

#renaming the file

# import os

# os.rename('python-basics-revision/File_Handling/ report.txt','report1.txt')

# deleting the file

import os
os.remove('python-basics-revision/File_Handling/delete.txt')
    

