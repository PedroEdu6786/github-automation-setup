import os

class GitHandler:
    
    def create_new_repo(self):
        os.system('git flow init')