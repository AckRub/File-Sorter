import os
import shutil # to change the file directory (os.rename() did not work)

path = str(input("Enter a path: "))
file_name = os.listdir(path)

for i in file_name: # every element in the path (both directories and files)
    index = i.find(".")

    file_type = i[index+1:index+8] # everything after the dot for example i have "text.txt" so the result is "txt"


    i_path = os.path.join(path,i) # original path + i


    if os.path.isfile(i_path) == True: # checks if the file is a file or a directory
        new_path = os.path.join(path,file_type) # new path + file type

        if not os.path.exists(new_path): # checks if the directory already exists
            os.mkdir(new_path) # makes a new dir and the name of the dir is the siomet

            shutil.move(i_path,new_path) # change the file directory

        else:
            shutil.move(i_path,new_path)


        quit
    quit



        