import xml.etree.ElementTree as ET
import argparse
import textwrap

parser = argparse.ArgumentParser(
    prog='slf_fabricator',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''\
       sport is set to Cycling by default,
           but it can be changed in Sigma data center program
       '''))

parser.add_argument("-g", "--gpx", dest="gpx", type=argparse.FileType('r', encoding='UTF-8'), required=True, help="gpx file")
parser.add_argument("-s", "--speed", dest="speed", type=int, help="speed in km/h cannot be used with --time")
parser.add_argument("-T", "--time", dest="time", type=int, help="length of activity in minutes cannot be used with --speed")
parser.add_argument("-o", "--output", dest="output", help="output file name")

args = parser.parse_args()