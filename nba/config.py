# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
import yaml
from pathlib import Path
from mydataclasses import Config

# Load config.yaml as a dictionary
config_dict = yaml.safe_load((Path(__file__).parent.parent / "config.yaml").read_text())
config = Config.model_validate(config_dict)


