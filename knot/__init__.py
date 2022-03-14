from pathlib import Path

from knot.configs import KnotConfig
from knot.generators.make_model import MakeModel
from knot.generators.startapp import StartApp
from knot.utils import get_toml_configs


class Knot:
    """
    A cli helper to alot of menial django task

    """

    def __init__(self):
        self.configs = KnotConfig(get_toml_configs(Path.cwd()))
        self.configs.base_directory=Path.cwd()
        self.configs.apps_directory=self.configs.base_directory.joinpath(self.configs.apps_directory)


    def config(self):
        """
        Shows current available configs of knot
        """

        print(self.configs)

    def startapp(self,app_name):
        """
        create new app in current project
        :param app_name: app name like products
        :return:
        """
        StartApp(self.configs,app_name=app_name).render()

    def make_model(self,app_name,model_name:str=None):
        """
        create a new model in specified app
        :param app_name: app name in which model should be created
        :param model_name: name of the model to create
        :return:
        title:char max_length:22 null blank default:'45343'
        """
        if not model_name:
            model_name=input("Enter your model name: ")
            print("Please enter filed name like name:type arg:value")
            # fields=[]
            # while True:
            #     field_info=input("")
            #     if not field_info:
            #         break
            #     fields.append(field_info)
            # print(model_name)
            # for field in fields:
            #     print(field)
            MakeModel(self.configs,app_name=app_name,model_name=model_name).render()