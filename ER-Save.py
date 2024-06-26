# ER-Save
# Version: 1.0
# Elden Ring character save file utility to back up character save files. This program will look for character save files and then copy them if found. This currently works for both Vanilla and Seemless Co-Op save files. Tested on Windows 11 PC.
# Designed by Ghost-In-The-Void in 2024
# https://github.com/Ghost-In-The-Void/ER-Save
#Libraries used
import os
import shutil
#Variables to define what file types to look for and assigning a "category" to the file type
extensions = ".sl2"
seemless_save = ".co2"
#Variable to define the path to the games save directory
directory = os.path.join(os.path.expanduser("~"), r'AppData\Roaming\EldenRing')
#function to locate the save paths
def find_saves(extension, directory):
    matches = []
    for root, _, saves in os.walk(directory):
        for file in saves:
            if file.endswith(extension):
                matches.append(os.path.join(root))
    return matches
saves_location = find_saves(extensions, directory)
saves_location_str = "".join(map(str, saves_location))
back_up_folder = os.path.join(os.path.expanduser("~"), "Documents")
print(f"Save files are here ==> {saves_location}")
#start of file search
for filename in os.listdir(saves_location_str):
    #Variable to assign file path
    file_path = os.path.join(saves_location_str, filename)
    #start of loop
    if os.path.isfile(file_path):
        #Variable to trim filename and leave only the extension
        extension = os.path.splitext(filename)[1].lower()
        #Check to see if trimmed file name is one of the expected extensions
        if extension in extensions:
            #Variable to create folder name
            folder_name = "Elden Ring Save Backups"
            #Variable to assign path for creating folder
            folder_path = os.path.join(back_up_folder, folder_name)
            #Creating folder using folder_path, if folder already exist no error will trigger
            os.makedirs(folder_path, exist_ok=True)
            #Variable to define destination of character file
            destination_path = os.path.join(folder_path, filename)
            #Copying the file to new location
            shutil.copy(file_path, destination_path)
            #Printing results of move
            print(f"Copied {filename} to {folder_name} folder.")
        if extension in seemless_save:
            folder_name = "Elden Ring Save Backups"
            #Variable to assign path for creating folder
            folder_path2 = os.path.join(back_up_folder, folder_name)
            #Create folder
            os.makedirs(folder_path2, exist_ok=True)
             #Variable to define destination of character file
            destination_path2 = os.path.join(folder_path2, filename)
            #Copying the file to new location
            shutil.copy(file_path, destination_path2)
            #Printing results of move
            print(f"Copied {filename} to {folder_name} folder.")
            
        else:
            #Printing files that are skipped
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        #Printing folder names that are skipped
        print(f"Skipped {filename}. It is a directory.")
#Successful migration of character files        
print(f"Character back up completed. Your backup save files are located here ==>" + '\x1b[6;30;42m' + fr"{back_up_folder}\{folder_name}" + '\x1b[0m' "<==")
print('\x1b[0;30;43m' + "Vanilla save files end in .sl2 and Seemless Co-op saves end in .co2" + '\x1b[0m')
input('Press Enter to exit....')

