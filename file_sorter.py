import os

path = input("please enter the starting directory: ")

file_list = os.listdir(path)

file_paths = []

file_types = {
    'Documents': ['.doc', '.docx', '.pdf', '.txt'],
    'Slideshows': ['.ppt', '.pptx'],
    'Spreadsheets': ['.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', 'png', '.'],
    'Videos': ['.mp4', '.avi', '.wmv', '.m4v'],
    'Audio': ['.mp3', '.wav', '.wav', '.wma'],
    'Program Files': ['.css', '.py', '.js', '.html'],
    'Other': []
}


def file_sorter(root_directory):
    """First creates folders"""
    for key in file_types:
        # accesses dictionary keys to create folders with relevant names
        folder = root_directory + "/" + key
        if not os.path.exists(folder):
            os.mkdir(folder)

    for file in file_list:
        file_paths.append(os.path.join(root_directory, file))
        print(file)

    print(file_paths)


file_sorter(path)
