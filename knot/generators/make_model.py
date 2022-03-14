from pathlib import Path

from knot.generators.base import BaseGenerator


class MakeModel(BaseGenerator):
    def render(self):
        model_text=self.render_template("model_model/model.jinja",model_name=self.model_name)
        model_file=self.configs.apps_directory.joinpath(self.app_name).joinpath("model.py").open(mode='a')
        model_file.write(model_text)
        model_file.close()
        print(model_text)