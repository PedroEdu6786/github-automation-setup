import os

class GithubHandler:
    
    def create_github_repo(self):
        os.system('gh repo create')