import sys
from src.validators.ArgsValidation import ArgsValidation

# Project Setup Controller class
# Receives model and view at constructor
# create_project method generates setup from models
class ProjectConfigurator:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def create_project(self):
        num_args = len(sys.argv)
    
        if not ArgsValidation.validate_num_args(num_args):
            self.view.error_dispose("Missing arguments, try again with project's name")
        
        project_name = sys.argv[1] # name of project to create
        
        try:
            self.create_project_folder(project_name)
            self.create_git_repo()
            self.create_github_repo()
            self.create_initial_commit()
            self.view.display_project_created()
            
        except OSError:
            self.view.error_dispose(f'Error to create project, {project_name} folder already exists')
    
    
    def create_project_folder(self, project_name):
        self.model.setup_dir(project_name)
        self.view.success_display(f"Successfully folder project {project_name}")
        
        
    def create_git_repo(self):
        self.view.display_title("Setting up git repository...")
        self.model.setup_git()
        self.view.clear_screen()
        
        
    def create_github_repo(self):
        self.view.display_title("Setting up github repository...")
        self.model.setup_github()
        self.view.clear_screen()
        
        
    def create_initial_commit(self):
        self.view.display_title("Pushing to github repository...")
        self.model.push_to_github()
        self.view.clear_screen()