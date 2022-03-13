from pathlib import Path
from typing import List

import tomli


def find_toml_files(path:Path)->List[Path]:
    knot_file="knot.toml"
    toml_files=[

    ]
    if path.joinpath(knot_file).exists():
        toml_files.append(path.joinpath(knot_file))
    for parent in path.parents:
        if parent.joinpath(knot_file).exists():
            toml_files.append(parent.joinpath(knot_file))
    return toml_files

def get_toml_configs(path:Path):
    toml_files=find_toml_files(path)
    if toml_files:
        with open(toml_files[0]) as toml_file:
            return tomli.loads(toml_file.read())
