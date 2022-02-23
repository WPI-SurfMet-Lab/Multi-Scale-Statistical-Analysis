import sys
sys.path.insert(0, '..')
from multiscale_modules.utils.read_data import *
from multiscale_modules.utils.interpolate import *

if __name__ == "__main__":
    args = sys.argv[1:]
    stat = args[0]
    data = []
    data.append(read_data('./../samples/sample1.txt'))
    data.append(read_data('./../samples/sample2.txt'))
    data.append(read_data('./../samples/sample3.txt'))
    data.append(read_data('./../samples/sample4.txt'))
    data.append(read_data('./../samples/area-scale-test-data.txt'))
    interpolate(data, stat)