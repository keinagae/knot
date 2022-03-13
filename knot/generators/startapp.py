from pathlib import Path

from knot.generators.base import BaseGenerator


class StartApp(BaseGenerator):
    name="startapp"
    template_files=[
        "__init__.py.jinja",
        "admin.py.jinja",
        "apps.py.jinja",
        "forms.py.jinja",
        "model.py.jinja",
        "urls.py.jinja",
        "views.py.jinja",
    ]

    def render(self):
        self.configs.apps_directory.mkdir(exist_ok=True)
        app_directory=self.configs.apps_directory.joinpath(self.app_name)
        app_directory.mkdir(exist_ok=True)
        for template_file in self.template_files:
            file=app_directory.joinpath(template_file.replace(".jinja","")).open(mode="w")
            file.write(self.render_template(self.name+"/"+template_file,app_name=self.app_name))
            file.close()