from typing import Dict
from abc import ABC,abstractmethod

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

    @abstractmethod
    def render(self):
        pass