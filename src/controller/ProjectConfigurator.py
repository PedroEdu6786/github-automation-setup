import sys
from src.validators.ArgsValidation import ArgsValidation
from src.model.FolderGenerator import FolderGenerator
from src.model.GitHandler import GitHandler
from src.model.GithubHandler import GithubHandler


class ProjectConfigurator:
    
    def __init__(self, model):
        self.model = model
    
    def create_project(self):
        num_args = len(sys.argv)
    
        if not ArgsValidation.validate_num_args(num_args):
            print("Number of arguments not valid")
            sys.exit()
        
        project_name = sys.argv[1] # name of project to create
        
        try:
            self.model.setup_dir(project_name)
            self.model.setup_git()
            self.model.setup_github()
            self.model.push_to_github()
        except OSError:
            print(f'Error to create project, {project_name} folder already exists')
    