import os
import shutil

def clean_desktop():
    # Specify the path to your desktop
    desktop_path = r'C:\Users\YourUsername\Desktop'

    # Specify the path to the folder where you want to move the files
    destination_folder = r'C:\Users\YourUsername\Desktop\CleanedDesktop'

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get a list of all files and directories on the desktop
    desktop_contents = os.listdir(desktop_path)

    # Move each file and directory to the destination folder
    for item in desktop_contents:
        item_path = os.path.join(desktop_path, item)
        dest_path = os.path.join(destination_folder, item)
        
        # Skip the destination folder and the current working directory
        if item_path == destination_folder or item_path == os.getcwd():
            continue
        
        try:
            shutil.move(item_path, dest_path)
        except PermissionError as e:
            print(f"PermissionError: Could not move {item_path}. Reason: {e}")
        except Exception as e:
            print(f"Error: Could not move {item_path}. Reason: {e}")

    print('Desktop cleaned successfully!')

# Call the clean_desktop function
clean_desktop()
