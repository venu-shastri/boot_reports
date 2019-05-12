import sys

def printusage_and_quit(argv):
    print("Usage: " + argv[0] + " <csv source folder>")
    sys.exit()

def parse_path(argv):
    if len(argv) != 2:
        printusage_and_quit(argv)
    source_directory = argv[1]
    return source_directory
