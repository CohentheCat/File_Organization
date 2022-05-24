from genericpath import exists
from msilib.schema import Error
import os
import collections
from pprint import pprint

#Selects the folder you want to sort

TARGET_PATH = os.path.join(os.path.expanduser("~"), 'Downloads')

#Will make folders for each file type in the given directory if one does not exist.
file_mappings = collections.defaultdict()
for file_name in os.listdir(TARGET_PATH):
    file_type = file_name.split('.')[-1]
    file_mappings.setdefault(file_type, []).append(file_name)

pprint(file_mappings)

#Will move all files to folders based on the file type
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(TARGET_PATH, folder_name)
    if not os.path.exists(folder_path):
        pprint(f"Need to make a {folder_path} folder!")
    
    for folder_item in folder_items:
        source = os.path.join(TARGET_PATH, folder_item)
        destination = os.path.join(folder_path, folder_item)
        pprint(f"Moving: {source} to {destination}")
        try:
            os.rename(source, destination)

        except FileExistsError:
            pprint("Sorry a file of this name exists in this folder")
        
        except PermissionError:
            pprint("Hang on a sec...")
