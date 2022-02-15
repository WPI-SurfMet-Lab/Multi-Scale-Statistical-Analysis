import pandas as pd


def read_data(file_name):
    with open(file_name, encoding='ISO-8859-1') as f:
        lines = f.readlines()
    lines = lines[5:]
    rows = [line.split("\t")[:-1] for line in lines]
    df = pd.DataFrame(rows, columns=["scale of analysis", "relative area", "fractal complexity", "r2"])
    return df
