import shutil

def organize_files(source_directory):
    # Define the categories and their corresponding folders
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.tar', '.gz'],
        'Others': []
    }

    # Create the category folders if they do not exist
    for category in categories:
        category_path = os.path.join(source_directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Organize files into their respective folders
    for filename in os.listdir(source_directory):
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        
        for category, extensions in categories.items():
            if file_extension in extensions:
                shutil.move(os.path.join(source_directory, filename), os.path.join(source_directory, category, filename))
                moved = True
                break
        
        if not moved and file_extension:
            # Move files with unknown extensions to 'Others'
            shutil.move(os.path.join(source_directory, filename), os.path.join(source_directory, 'Others', filename))

    print("Files have been organized successfully.")

if __name__ == "__main__":
    # Specify the directory you want to organize
    source_directory = input("Enter the path of the directory to organize: ")
    if os.path.isdir(source_directory):
        organize_files(source_directory)
    else:
        print("Invalid directory path.")