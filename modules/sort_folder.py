import os
import shutil

def sort_documents(folder):
    for file_name in os.listdir(folder):
        source = os.path.join(folder, file_name)
        if os.path.isfile(source):
            extension = os.path.splitext(file_name)[1]
            if extension == ".log":
                logs_folder = os.path.join(folder, "logs")
                if not os.path.exists(logs_folder):
                    os.makedirs(logs_folder)
                destination = os.path.join(logs_folder, file_name)
                shutil.move(source, destination)
            elif extension == ".eml":
                mail_folder = os.path.join(folder, "mail")
                if not os.path.exists(mail_folder):
                    os.makedirs(mail_folder)
                destination = os.path.join(mail_folder, file_name)
                shutil.move(source, destination)
            # Add more file extensions and corresponding folders if needed

# Usage:
sort_documents("documents_folder")
