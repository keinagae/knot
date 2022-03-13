from typing import Dict
from abc import ABC,abstractmethod
from jinja2 import Environment, PackageLoader, select_autoescape

from knot import KnotConfig


class BaseGenerator(ABC):
    """
    Base class for generators
    """
    def __init__(self, configs: KnotConfig,**kwargs):
        """

        :param configs: configs read from knot file
        """
        self.configs = configs
        for arg, value in kwargs.items():
            setattr(self, arg,value )
        self.jinja = Environment(
            loader=PackageLoader("knot"),
            autoescape=select_autoescape()
        )

    def render_template(self,template_name,**kwargs):
        """
        renders template files from knot template directory
        :param template_name: name of template file
        :param kwargs:
        :return: str
        """
        template=self.jinja.get_template(template_name)
        return template.render(**kwargs,apps_directory=self.configs.apps_directory.name)

    @abstractmethod
    def render(self):
        pass