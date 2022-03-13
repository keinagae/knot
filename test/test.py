import sys
from pathlib import Path
import fire
from knot import Knot


BASE_DIRECTORY=Path(__file__).parent.parent
sys.path.append(str(BASE_DIRECTORY.absolute()))


if __name__ == '__main__':
    fire.Fire(Knot)