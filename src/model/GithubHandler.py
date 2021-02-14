import os
from src.constants.GithubCommands import GithubCommands

class GithubHandler:
    
    def create_github_repo(self):
        create_repo = GithubCommands.CREATE_REPO
        public_flag = GithubCommands.PUBLIC_FLAG
        
        create_repo_command = f'{create_repo} {public_flag}'
        os.system(create_repo_command)