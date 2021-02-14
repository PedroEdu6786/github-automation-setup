import os
from src.constants.GitCommands import GitCommands

class GitHandler:
    
    def create_new_repo(self):
        os.system(GitCommands.INIT_FLOW)
    
    def add_changes(self):
        os.system(GitCommands.ADD_CHANGES)
        
    def initial_commit(self):
        os.system(GitCommands.INITIAL_COMMIT)
        
    def push_changes(self):
        os.system(GitCommands.PUSH_MAIN)
        os.system(GitCommands.PUSH_DEVELOP)
        
    def repo_setup(self):
        self.add_changes()
        self.initial_commit()
        self.push_changes()