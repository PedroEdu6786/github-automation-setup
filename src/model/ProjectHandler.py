from src.model.GitHandler import GitHandler
from src.model.GithubHandler import GithubHandler
from src.model.FolderGenerator import FolderGenerator

class ProjectHandler:
    def __init__(self, folder_handler, git, github):
        self.git = git
        self.github = github
        self.folder_handler = folder_handler
        
    def setup_dir(self, file_name):
        folder_handler = self.folder_handler
        folder_handler.generate_folder(file_name)
        folder_handler.navigate_to_folder(file_name)
        
    def setup_git(self):
        self.git.create_new_repo()
        
    def setup_github(self):
        self.github.create_github_repo()
        
    def push_to_github(self):
        self.git.repo_setup()
