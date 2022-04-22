import csv
import re
import pandas as pd


with open('text1.txt', "r", encoding='utf-8') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('main2.csv', 'w', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Name', '           ', 'Phone', '         ', 'Mobile', '               ',
                        'Email', '              ', 'Address'))

    with open("text1.txt", encoding='utf-8') as file:
        lines = [line for line in file]
        count = 0
        for row in lines:
            df = pd.read_csv("main2.csv")
            count += 1
            if row.startswith("[+91]"):
                df.loc[count, 'Mobile'] = str(row)
                df.to_csv("main2.csv", index=False)
            elif row.startswith("[+91] ("):
                df.loc[count, 'Phone'] = str(row)
                df.to_csv("main2.csv", index=False)
            elif 'CA.' in row:
                df.loc[count, 'Name'] = str(row)
                df.to_csv("main2.csv", index=False)
            elif '@' in row:
                df.loc[count, 'Email'] = str(row)
                df.to_csv("main2.csv", index=False)

            elif row[0].isdigit():
                df.loc[count, 'Address'] = str(row)
                df.to_csv("main2.csv", index=False)

            else:
                continue
