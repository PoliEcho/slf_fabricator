import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-g", "--gpx",dest ="gpx", help="gpx file")
parser.add_argument("-t", "--temperature",dest = "temperature", help="temperature during activity")
parser.add_argument("-c", "--calories",dest = "calories", help="calories burned during activity")


args = parser.parse_args()