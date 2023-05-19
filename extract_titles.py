import csv
import os

#CSV files
directory = './csv_text2'

output_file = open('./all_caption2.csv', 'a', encoding='utf-8') 

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, encoding='utf-8', errors='replace') as csv_file:
            print(f)
            csv_reader = csv.reader(csv_file, delimiter='|')
            line_count = 0
         
            for row in csv_reader:
                if line_count != 0:
                  #  print(row[4])     
                    output_file.write("{0}".format(row[11]))
                   # output_file.write("{0}".format(row[6]))
                line_count += 1


output_file.close()
# need to extract the ID
# need to extrace the 
