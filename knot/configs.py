from pathlib import Path


class KnotConfig(object):
    base_directory:Path
    apps_directory:Path
    def __init__(self, configs):
        for key,value in configs.items():
            setattr(self,key,value)

