import sys
from multiscale_modules.utils.read_data import read_data
from multiscale_modules.utils.interpolate import interpolate

if __name__ == "__main__":
    args = sys.argv[1:]
    stat = args[0]
    data = [read_data('./../samples/sample1.txt'),
            read_data('./../samples/sample2.txt'),
            read_data('./../samples/sample3.txt'),
            read_data('./../samples/sample4.txt'),
            read_data('./../samples/area-scale-test-data.txt')]
    interpolate(data, stat)
