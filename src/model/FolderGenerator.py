import os

class FolderGenerator:
        
    def __init__(self):
        self.path = os.getcwd()
        
    def generate_folder(self, folder_name):
        
        folder_path = f'{self.path}/{folder_name}'
        try:
            os.mkdir(folder_path)
        except OSError:
            print(f'Error to create folder {folder_name}')
            
        print(f'Successfully created folder {folder_name}')