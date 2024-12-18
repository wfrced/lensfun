import argparse
import glob
import os

import xml_converter

# Generates files needed for updating lensfun data with "lensfun-update-data".

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate files for the Lensfun database updates "
                                                 "(tar balls for all Lensfun versions).")
    parser.add_argument("-i", "--input", default="data/db/", help="input folder containing XML files")
    parser.add_argument("-o", "--output", default="db/", help="output folder for generated db")
    parser.add_argument("-t", "--timestamp", type=int, default=None, help="Timestamp to use for file modification times")
    args = parser.parse_args()

    xml_filenames = glob.glob(os.path.join(args.input, "*.xml"))
    xml_files = set(xml_converter.XMLFile(filename) for filename in xml_filenames)

    if args.timestamp is not None:
        timestamp = args.timestamp
    else:
        # Fallback to SOURCE_DATE_EPOCH for reproducible builds
        timestamp = int(os.environ.get("SOURCE_DATE_EPOCH", "0"))

    print(timestamp)

    xml_converter.generate_database_tarballs(xml_files, timestamp, args.output)
