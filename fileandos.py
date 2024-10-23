import os
from pathlib import Path
import glob
# myfile=open("note.txt", "r")
# print(myfile.read())
# myfile.close()

# myfile=open("C:\\Users\\Lenovo\\Documents\\fileopeningexample.txt", "r")
# print(myfile.read())
# myfile.close()

# with open("C:\\Users\\Lenovo\\Documents\\fileopeningexample.txt", "r") as file:
#     content=file.read()
#     print(content)

# file mode
'''
r - read only
w - write
w+ - write
a - append
x - create
'''

# with open("note2.txt", "w+") as file:
#     content=file.write('i am the eraser you are looking for......min pa2')
#     print("job done")
#     content=file.read()

#     print(content)

# with open("note2.txt", "r") as file:
# with open("note2.txt", "r+") as file:
#     content=file.write(' one day ona day one day pamilekeji....')
#     print("job done")
#     content=file.read()

#     # content=file.read()

#     print(content)

# with open("C:\\Users\\Lenovo\\Documents\\example12.pdf", "x") as file:
#     file.write("hellooooo i an m=the new file")
#     print('done')

# pip install PyPDF2
# from PyPDF2 import PdfReader
# reader = PdfReader("C:\\Users\\Lenovo\\Documents\\example12.pdf")
# number_of_pages = len(reader.pages)
# print(number_of_pages)
# for page in range(len(reader.pages)):
#     page = reader.pages[page]
#     text = page.extract_text()
#     print(text)

# with open(r"C:\Users\Lenovo\Downloads\sqi.csv", "r") as file:  
#     data = file.read()
#     print(data, "an excel file"  )

# with open(r"C:\Users\Lenovo\Downloads\edited_output4.tsv", "r", encoding='utf-8') as file:  
#     data = file.read()
#     print(data, "an excel file"  )

# with open("note2.txt", "r+") as file:
#     content = file.read()
#     print(content)
    # print(file.write("  this mode is a special mode\n"))
    # print(content)

    
# with open("note2.txt", "r+") as file:
#     content = file.read()  # Read the entire file content
#     file.seek(0, 2)  # Move the file pointer to the end of the file
#     file.write("this mode is a special mode\n")  # Write to the file
#     file.seek(0)  # Move the file pointer back to the beginning
#     updated_content = file.read()  # Read the file again to get updated content
#     print(updated_content)








# os interaction
# num_of_dir=os.scandir()
# for files in   num_of_dir:
#     print('files name: ',files)
# print(num_of_dir)

# list_my_files = os.scandir()
# with os.scandir(r'C:\Allproject') as  list_dir_content:
#     for files in   list_dir_content:
#         print('files name: ',files)
# print(type(files))


# print(list_dir_content)
# all_path=Path()

# list_dir_content=Path()
# for entry in list_dir_content.iterdir():
#     print(entry)
# print(type(entry))

# list_dir_content=Path(r'C:\Allproject')
# for entry in list_dir_content.iterdir():
#     print(entry)
# print(type(entry))

# new_dir=os.mkdir('first_folder')
# print('done')


# Making Directories
# new_dir2=os.mkdir(r'C:\python_pclass\newfolder2')   #
# print("done")

# os.mkdir('C:\\python-pclass\\goodness\\example4.pdf')
# print("done")
# myfile2='example6.csv'

# with open(r'C:\python_pclass\newfolder2\myfile2.txt', 'x', encoding='utf-8') as file:
#     file.write("creating a new file using the x mode")
#     # print(file.read())
#     print('done')

# with open(r'C:\\python_pclass\\newfolder1\\myfile2', 'r', encoding='utf-8') as file:
#     # file.write("creating a new file using the x mode")
#     print(file.read())
#     # print('done')


# directory_path='folder3'

# if not os.path.exists(directory_path):
#     # If it doesn't exist, create it
#     os.makedirs(directory_path)
#     with open("folder3\myfile1", "w") as file:
#         file.write("helooooooooooooo")
#         print('text written successfully')
#         print("Directory created successfully")
# else:
#     print("Directory already exists")


# file_path = os.path.join(r"C:\python-works2", 'example5.py')

# # Check if the file already exists
# if not os.path.exists(file_path):
#     # If it doesn't exist, create it
    # os.makedirs(file_path)
#     with open(file_path, 'w') as file:
#         # You can optionally write something to the file
#         file.write("This is a py file created using Python!")
#     print("File created successfully")
# else:
#     print("File already exists")


# Filename Pattern Matching Using glob
# print(glob.glob('*.txt'))
# for file in glob.iglob('**/*.py', recursive=True):
#     print(file)


# for dirpath, dirnames, files in os.walk('.'):
#     print(f'i am >>{dirnames}')
#     print(f'Available directory: {dirpath}')
#     for file_name in files:
#         print(file_name, 'files')
#     print()

