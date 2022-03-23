import csv
import os
import re
import argparse


def read_write_File(infile, outfile):
    # because our infile is set to work on "feed_sample.csv", I changed the file name to "feed2"
    pattern1 = re.compile('(.*jumper.*)', re.IGNORECASE)
    os.rename("feed_sample.csv", infile)
    pattern2 = re.compile(r'.*(?:(jumper)|^).*?knit.*?(?:(jumper)|$)', re.IGNORECASE)
    pattern = re.compile('^((?!.*jumper).).*(?=.*knit.*)', re.IGNORECASE)
    with open(infile, 'r', encoding="utf-8") as bigCSV, \
            open(outfile, 'w', encoding="utf-8", newline='') as write_obj:
        csv_reader = csv.reader(bigCSV)
        csv_writer = csv.writer(write_obj)
        headFlag = True
        for row in csv_reader:
            if headFlag:
                header = row
                csv_writer.writerow(header)
                headFlag = False
            else:
                if (pattern2.search(line) for line in row):
                    # if not any(pattern1.match(line) for line in row):
                    csv_writer.writerow(row)
    os.rename(infile, "feed_sample.csv")  # changing the name back, so we can keep working on feed_sample


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str)
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    read_write_File(args.infile, args.out)


if __name__ == '__main__':
    main()
