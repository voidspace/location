import argparse
from location import NetworkSource, LocationStore

parser = argparse.ArgumentParser("Calculate distances between locations")
parser.add_argument("start")
parser.add_argument("finish")
parser.add_argument("--display")
args = parser.parse_args()

source = NetworkSource("http://voidspace.org.uk/coords.txt")
store = LocationStore("txt")
store.fetch_places(source)
print("{:.2f} kilometers".format(store.distance(args.start, args.finish)))
