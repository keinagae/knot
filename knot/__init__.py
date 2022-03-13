from pathlib import Path

from knot.utils import get_toml_configs


class Knot(object):
    """
    A cli helper to alot of menial django task

    """

    def config(self):
        """
        Shows current available configs of knot
        """
        configs=get_toml_configs(Path.cwd())
        print(configs)
