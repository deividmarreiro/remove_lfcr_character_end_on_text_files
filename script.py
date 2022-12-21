import argparse
import glob
import os

parser = argparse.ArgumentParser()

parser.add_argument("--onefile", help="Path to the txt files")

args = parser.parse_args()

txt_files = glob.glob(os.path.join(args.onefile, "*.txt"))

for txt_file in txt_files:
    with open(txt_file, "r") as f:
        # Read the contents of the file
        contents = f.read()
    contents = contents.replace("\n\r", "\n")
    with open(txt_file, "w") as f:
        f.write(contents)