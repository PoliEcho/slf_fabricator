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

parser.add_argument("-g", "--gpx", dest="gpx", help="gpx file")
parser.add_argument("-t", "--temperature", dest="temperature", help="temperature during activity")
parser.add_argument("-s", "--speed", dest="speed", help="speed in km/h cannot be used with --time")
parser.add_argument("-T", "--time", dest="time", help="length of activity cannot be used with --speed")
parser.add_argument("-o", "--output", dest="output", help="output file name")

args = parser.parse_args()
