import pandas as pd
import os
import numpy as np


def read_data(file_name: str) -> pd.DataFrame:
    with open(file_name, encoding='ISO-8859-1') as f:
        lines = f.readlines()
    lines = lines[5:]

    # Store data from file lines
    rows = [line.split("\t")[:-1] for line in lines]
    df = pd.DataFrame(rows, columns=["scale of analysis", "relative area", "fractal complexity", "r2"])

    # Convert data columns into floats
    df = df.astype('float')

    return df

def load_data(folder, filename):
    """ Loads data from the specified folder and filename

    Args:
        folder (string): the folder name in the project directory
        filename (string): the name of the file to load in

    Returns:
        df (pd.DataFrame): the resulting dataframe after reading in the data from the file
    """
    data = np.loadtxt(os.path.join(folder, filename), dtype=float, skiprows=4)
    df = pd.DataFrame(data, columns=["scale_of_analysis", "relative_area", "fractal_complexity", "r2"])
    return df
