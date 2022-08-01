import argparse

parser = argparse.ArgumentParser(description="The following is a help document")
parser.add_argument('--add', action='store', dest='invest', help='add a new invest')
args = parser.parse_args()
invest = (args.invest)
if (invest != None):
    print('Input: ' + invest )
    exit(0)
print('Hello World!')