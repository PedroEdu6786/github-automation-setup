from src.model.FolderGenerator import FolderGenerator
from src.model.GitHandler import GitHandler
from src.model.GithubHandler import GithubHandler
from src.model.ProjectHandler import ProjectHandler
from src.controller.ProjectConfigurator import ProjectConfigurator


if __name__ == "__main__":
    
    model = ProjectHandler(FolderGenerator(), GitHandler(), GithubHandler())
    
    project = ProjectConfigurator(model)
    
    project.create_project()