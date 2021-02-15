from src.model.FolderGenerator import FolderGenerator
from src.model.GitHandler import GitHandler
from src.model.GithubHandler import GithubHandler
from src.model.ProjectHandler import ProjectHandler
from src.view.SetupUI import SetupUI
from src.controller.ProjectConfigurator import ProjectConfigurator


if __name__ == "__main__":
    
    model = ProjectHandler(FolderGenerator(), GitHandler(), GithubHandler())
    view = SetupUI()
    
    #Project setup controller logic
    project = ProjectConfigurator(model, view)
    
    #Creates new project
    project.create_project()