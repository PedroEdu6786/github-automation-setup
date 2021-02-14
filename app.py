import sys
from src.validators.ArgsValidation import ArgsValidation
from src.model.FolderGenerator import FolderGenerator
from src.model.GitHandler import GitHandler


if __name__ == "__main__":
    num_args = len(sys.argv)
    
    if not ArgsValidation.validate_num_args(num_args):
        print("Number of arguments not valid")
        sys.exit()
    
    file_argument = sys.argv[1] # name of project to create
    
    folder_name = FolderGenerator()
    folder_name.generate_folder(file_argument)
    folder_name.navigate_to_folder(file_argument)
    git = GitHandler()
    git.create_new_repo()