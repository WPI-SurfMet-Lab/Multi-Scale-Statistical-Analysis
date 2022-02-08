import pandas as pd
import os

class DataReader():

    def __init__(self):
        return None

    def read(self, file_name):
        current_dir = "samples/"
        file_path = os.path.join(current_dir, file_name)
        with open(file_path) as f:
            lines = f.readlines()
        lines = lines[4:]
        rows = [line.split("\t")[:-1] for line in lines]
        df = pd.DataFrame(rows, columns=["scale of analysis", "relative area", "fractal complexity", "r2"])
        return df
