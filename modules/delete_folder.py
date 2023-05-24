import os
import shutil

def move_user_documents(user_folder, temp_folder):
    if os.path.exists(user_folder):
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        for file_name in os.listdir(user_folder):
            source = os.path.join(user_folder, file_name)
            destination = os.path.join(temp_folder, file_name)
            shutil.move(source, destination)
        print(f"Moved user's documents to '{temp_folder}' successfully.")
    else:
        print(f"User folder '{user_folder}' does not exist.")

# Usage:
move_user_documents("user2", "temp_folder")
