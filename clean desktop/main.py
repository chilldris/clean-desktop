import os
import shutil

def clean_desktop():
    desktop_path = r'C:\Users\YourUsername\Desktop'

    destination_folder = r'C:\Users\YourUsername\Desktop\CleanedDesktop'

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    desktop_contents = os.listdir(desktop_path)

    for item in desktop_contents:
        item_path = os.path.join(desktop_path, item)
        dest_path = os.path.join(destination_folder, item)

        if item_path == destination_folder or item_path == os.getcwd():
            continue
        
        try:
            shutil.move(item_path, dest_path)
        except PermissionError as e:
            print(f"PermissionError: Could not move {item_path}. Reason: {e}")
        except Exception as e:
            print(f"Error: Could not move {item_path}. Reason: {e}")

    print('Desktop cleaned successfully!')

clean_desktop()

