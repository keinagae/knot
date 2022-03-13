from pathlib import Path

from knot.generators.base import BaseGenerator


class StartApp(BaseGenerator):

    def render(self):
        self.configs.apps_directory.mkdir(exist_ok=True)
        app_directory=self.configs.apps_directory.joinpath(self.app_name)
        app_directory.mkdir(exist_ok=True)
        app_directory.joinpath("model.py").open(mode="w")
        app_directory.joinpath("admin.py").open(mode="w")
        app_directory.joinpath("apps.py").open(mode="w")
        app_directory.joinpath("__init__.py").open(mode="w")
        app_directory.joinpath("views.py").open(mode="w")
        app_directory.joinpath("urls.py").open(mode="w")
        app_directory.joinpath("forms.py").open(mode="w")