import pandas as pd


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
