import csv
import time
from collections import defaultdict
from itertools import chain

# import raw data into input_file
try:
    with open("./input/itcont.txt") as f:
        input_file = csv.reader(f)
        header = next(input_file) # skip header
        input_file = list(input_file)
except IOError as e:
    print('File does not exist or no permissions.')
    exit()

'''
Data preparing and cleaning:

Create a 2-D list with cleaned and sorted records from the raw txt file.
Each row includes the drug name, concatenated prescriber name, and drug cost from the raw data.

Return [input_records]: 
columns: [drug_name, prescriber_name(last+first, upper-cased), drug_cost]
rows: sorted by drug_name then by prescriber_name
'''
start_time = time.time()
input_records=[]

for records in input_file:
    input_records.append([records[3], (records[1]+' '+records[2]).upper(), records[4]])

input_records.sort(key=lambda x: (x[0], x[1]))

data_time = time.time()
print ('Data preparation took {0} seconds to run!'.format(round((data_time-start_time),4)))


'''
Calculate number of prescribers (num_prescriber):

Create a dictionary contains the number of unique prescribers for each drug

Return {prescriber_num}: 
key: 'drug_name'
value: float(num_prescriber)
a. first create a list of unique prescriber names for each drug
b. then get the length of each list from a.
'''
from collections import defaultdict

# create a dictionary defaults to list
prescriber_number = defaultdict(list) 

# step a.
for k, v1, v2 in input_records:
    if v1 not in prescriber_number[k]:
        prescriber_number[k].append(v1)
# step b.
for k in prescriber_number.keys():
    prescriber_number[k] = len(prescriber_number[k])

presnum_time = time.time()
print ('Prescriber number took {0} seconds to run!'.format(round((presnum_time-data_time),4)))


'''
Calculate total drug cost (total_cost):

Create a dictionary contains total drug cost for each drug.
Print warning message if the record doesn't have a valid drug cost, and continue.
(ValueError: could not convert string to float:)

Return {drug_cost}: 
key: 'drug_name'
value: float(total_cost)
'''
# create a dictionary defaults to float
drug_cost = defaultdict(float)

# add all drug cost entries for every drug
for k, v1, v2 in input_records:
    try:
        drug_cost[k] += float(v2)
    except ValueError:
        print('Cost for drug {0} prescribed by {1} is missing, thus treated as 0 dollar.'.format(k, v1))
        continue

drugcost_time = time.time()
print ('Drug cost took {0} seconds to run!'.format(round((drugcost_time-presnum_time),4)))


'''
Create the final sorted drug table list:

a. merge 2 dictionaries {drug_cost}+{prescriber_number} by the same key 'drug_name' to {drug_table}
b. sort {drug_table} by 'drug_cost' (descending-), then by 'drug_name' (ascending+)

Return: [drug_table_sorted]
columns: [drug_name, [prescriber_number, drug_cost]]
rows: sorted by drug_cost(-drug_table.values[1]) then by drug_name(+drug_table.keys)
'''
from itertools import chain

# create a dictionary drug_table default to list
drug_table = defaultdict(list)

# step a.
for a, b in chain(prescriber_number.items(), drug_cost.items()):
    drug_table[a].append(b)
# step b.
drug_table_sorted = sorted(drug_table.items(), key=lambda kv: (-kv[1][1], kv[0]))

table_time = time.time()
print ('Final sorted table took {0} seconds to run!'.format(round((table_time - drugcost_time),4)))


#  define header and write the final sorted drug table to the output dictory as top_cost_drug.txt
output_header = ['drug_name', 'num_prescriber', 'total_cost']

try:
    with open('./output/top_cost_drug.txt', 'w') as f:
        output_file = csv.writer(f)
        output_file.writerow(output_header)
        for i in range(len(drug_table_sorted)):
            output_file.writerow([drug_table_sorted[i][0],(drug_table_sorted[i][1][0]),int(round(drug_table_sorted[i][1][1]))])
except IOError as e:
    print('No permission to write file.')
    exit()

print ('In total pharmacy_counting.py took {0} seconds to run!'.format(round((time.time() - start_time),4)))
