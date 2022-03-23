import argparse
import csv
import os
import pandas as pd


def list_of_str_to_num(list1):
    list1 = [float(w.replace("USD ", '')) for w in list1]
    return list1


def create_File(filename):
    csv_table = pd.read_table(filename, sep="\t")
    csv_table.to_csv('tmp.csv', index=False)


def edit_File(outfile):
    reader1 = pd.read_csv('tmp.csv')
    priceRow = reader1['price'].tolist()
    editedPrice = list_of_str_to_num(priceRow)
    header_of_new_col = "price_edited"
    add_column_in_csv('tmp.csv', outfile,
                      lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else
                      row.append(editedPrice[line_num - 2]))


def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r', encoding="utf-8") as read_obj, \
            open(output_file, 'w', encoding="utf-8", newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = csv.reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str)
    parser.add_argument('--out', type=str)
    args = parser.parse_args()
    create_File(args.infile)
    edit_File(args.out)
    os.remove("tmp.csv")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
