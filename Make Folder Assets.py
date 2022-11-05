# Make Project Folder
#For 3ds max And C4d By 'IMANSHIRANI'

# importing os module
import os

# Directory

list = ['00_Assets', '01_scenes', '06-Composit', '07-Texture', '08-Export', '09-archive', '10_Render']
  

# Parent Directory path
parent_dir = "F:/3DSMAX SCRIPT/Project Assets/"


def createFolder():
    for items in list:
        # Path
        path = os.path.join(parent_dir, items)
        
        try:
            os.mkdir(path, os.path.exists == True)
            print("Directory '% s' created" % list)
            print("Directory '%s' created successfully" % list)
        except OSError as error:
            print("Directory '%s' can not be created" % list)
            print("The Directory Was Exists")
       
        

# Create Folders
createFolder()


