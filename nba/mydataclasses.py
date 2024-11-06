# TODO: define your data classes here
from typing import List
from pydantic import BaseModel


# Define DataConfig to match the "data" section
class DataConfig(BaseModel):
    table: str
    data_path: str
    features_columns: List[str]

# Define ParamConfig to match the "params" section within "model"
class ParamConfig(BaseModel):
    max_iter: int
    random_state: int

# Define ModelConfig to match the "model" section
class ModelConfig(BaseModel):
    name: str
    type: str
    params: ParamConfig

# Define the root Config class to match the entire config.yaml structure
class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
