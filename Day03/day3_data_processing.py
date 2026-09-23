from extract_data import extract_data
from transform_data import transform_data
from load_data import load_data

data = extract_data()
transformed_data = transform_data(data)
load_data(transformed_data)