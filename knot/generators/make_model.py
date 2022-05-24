from pathlib import Path

from knot.generators.base import BaseGenerator


class MakeModel(BaseGenerator):

    TEMPLATE_FILES = {
        "model":"model.py"
    }

    def render(self):
        model_text=self.render_template("model_model/model.jinja",model_name=self.model_name,fields=self.fields)
        with open(self.configs.apps_directory.joinpath(self.app_name).joinpath(self.TEMPLATE_FILES['model']),mode='a') as file:
            file.write(model_text)