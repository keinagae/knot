from pathlib import Path

from knot.generators.base import BaseGenerator


class StartApp(BaseGenerator):
    name="startapp"
    TEMPLATE_FILES={
        "init":"__init__.py.jinja",
        "admin":"admin.py.jinja",
        "app":"apps.py.jinja",
        "forms":"forms.py.jinja",
        "model":"model.py.jinja",
        "urls":"urls.py.jinja",
        "views":"views.py.jinja",
    }

    def render(self):
        self.configs.apps_directory.mkdir(exist_ok=True)
        app_directory=self.configs.apps_directory.joinpath(self.app_name)
        app_directory.mkdir(exist_ok=True)
        for template_file in self.TEMPLATE_FILES.values():
            file=app_directory.joinpath(template_file.replace(".jinja","")).open(mode="w")
            file.write(self.render_template(self.name+"/"+template_file,app_name=self.app_name))
            file.close()

    def app_exists(self):
        app=self.configs.apps_directory.joinpath(self.app_name)
        if app.exists():
            return True
        return False