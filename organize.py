import os
import collections
from pprint import pprint

#Selects the folder you want to sort
folder_to_sort = 'Downloads'
TARGET_PATH = os.path.join(os.path.expanduser("~"), folder_to_sort)

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
        os.mkdir(folder_path)
    
    for folder_item in folder_items:
        source = os.path.join(TARGET_PATH, folder_item)
        destination = os.path.join(folder_path, folder_item)
        pprint(f"Moving: {source} to {destination}")
        try:
            if source != destination:
                os.rename(source, destination)

        except FileExistsError:
            pprint("Sorry a file of this name exists in this folder")
            pprint(f"Leaving {source} where it is...")
        
        except PermissionError:
            pprint("Hang on a sec...")

