# ER-Save
# Version: 1.11
# Elden Ring character save file utility to back up character save files. This program will look for character save files and then copy them if found. This currently works for both Vanilla and seamless Co-Op save files. Tested on Windows 11 PC.
# Designed by Ghost-In-The-Void in 2024
# https://github.com/Ghost-In-The-Void/ER-Save

# Libraries used
import os
import shutil
import logging

logging.basicConfig(filename="ER-SaveLog.log", filemode="w", format="%(name)s - %(levelname)s: %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)
FileOutputHandler = logging.FileHandler('logs.log')
logger.addHandler(FileOutputHandler)

try:
    # Variables to define what file types to look for and assigning a "category" to the file type
    extensions = ".sl2"
    seamless_save = ".co2"
    # Variable to define the path to the games save directory
    logger.info("Defining user Elden Ring folder location")
    directory = os.path.join(os.path.expanduser("~"), r'AppData\Roaming\EldenRing')

    # Function to locate the save paths
    logger.info("Locating save files")
    def find_saves(extension, directory):
        matches = []
        for root, _, saves in os.walk(directory):
            for file in saves:
                if file.endswith(extension):
                    matches.append(os.path.join(root))
        return matches

    logger.info("Files found")
    saves_location = find_saves(extensions, directory)
    logger.info("File path saved")
    saves_location_str = "".join(map(str, saves_location))
    logger.info("File path converted to str")
    back_up_folder = os.path.join(os.path.expanduser("~"), "Documents")
    logger.info("Backup folder Location established")
    print(f"Save files are here ==> {saves_location}")

    # Start of file search
    for filename in os.listdir(saves_location_str):
        try:
            # Variable to assign file path
            file_path = os.path.join(saves_location_str, filename)
            logger.info("file_path found")
            
            # Start of loop
            if os.path.isfile(file_path):
                # Variable to trim filename and leave only the extension
                extension = os.path.splitext(filename)[1].lower()
                logger.info("Extension trimmed from file name")

                # Check to see if trimmed file name is one of the expected extensions
                if extension in extensions:
                    logger.info("Extension is expected")
                    # Variable to create folder name
                    folder_name = "Elden Ring Save Backups"
                    # Variable to assign path for creating folder
                    folder_path = os.path.join(back_up_folder, folder_name)
                    # Creating folder using folder_path, if folder already exist no error will trigger
                    os.makedirs(folder_path, exist_ok=True)
                    logger.info("Created folder for Vanilla save back ups")
                    # Variable to define destination of character file
                    destination_path = os.path.join(folder_path, filename)
                    logger.info("Vanilla Character file destination established")
                    # Copying the file to new location
                    shutil.copy(file_path, destination_path)
                    logger.info("File copied to destination")
                    # Printing results of move
                    print(f"Copied {filename} to {folder_name} folder.")

                if extension in seamless_save:
                    folder_name = "Elden Ring Save Backups"
                    # Variable to assign path for creating folder
                    folder_path2 = os.path.join(back_up_folder, folder_name)
                    # Create folder
                    os.makedirs(folder_path2, exist_ok=True)
                    logger.info("Created folder for Seamless save back ups")
                    # Variable to define destination of character file
                    destination_path2 = os.path.join(folder_path2, filename)
                    logger.info("Seamless save file destination set")
                    # Copying the file to new location
                    shutil.copy(file_path, destination_path2)
                    logger.info("Seamless save file copied over")
                    # Printing results of move
                    print(f"Copied {filename} to {folder_name} folder.")

                else:
                    # Printing files that are skipped
                    print(f"Skipped {filename}. Unknown file extension.")
                    logger.info("Skipping the unwanted files")
            else:
                # Printing folder names that are skipped
                print(f"Skipped {filename}. It is a directory.")
                logger.info("Skipping the unwanted folders")
        except Exception as e:
            logger.exception(f"An error occurred while processing the file: {filename}")

    # Successful migration of character files
    print(f"Character back up completed. Your backup save files are located here ==> " + '\x1b[6;30;42m' + fr"{back_up_folder}\{folder_name}" + '\x1b[0m' + "<==")
    logger.info("Great success, folder location listed")
    print('\x1b[0;30;43m' + "Vanilla save files end in .sl2 and seamless Co-op saves end in .co2" + '\x1b[0m')
    logger.info("Great success, info on converting saves")
    input('Press Enter to exit....')
    logger.info("Program exited with Enter press")

except Exception as e:
    logger.exception("An error occurred in the main script")
