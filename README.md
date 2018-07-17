## Insight Data Engineer Pharmacy Counting Challenge

#### Python standard libraries used - 

- csv:  
  To read and process the input file.

- time:  
  To track time spent in each step.

- collections/defaultdict:  
  Instead of the default 'dict' object, I used 'defaultdict' to store prescriber and drug cost information for each unique drug.

- itertools/chain:  
  To merge 2 defaultdict objects into the final drug table.


#### pharmacy_count.py - 

In addition to the first (read and test input file) and the last (write and test output file) parts, this code includes 4 steps:

    1. Data preparation and cleaning to create a sorted [drug_name, prescriber_name, drug_cost] list
    2. Calculate number of unique prescribers for each drug {dict with drug_name as the key}
    3. Calculate total cost for each drug {dict with drug_name as the key}
    4. Combine two dictionaries and sort the final drug table


#### Environment - 

Sierra v.10.12.6  
MacBook Air mid 2011  
Processor 1.7 GHz Intel Core i5  
Memory 4 GB 1333 MHz DDR3  


#### Performance test - 

I tested the code with input data of 5, 1k, and 100k records.  All three tests finished within a reasonable timeframe.  I also tried the 24.5m records dataset, but it failed to finish in 20 minutes.  From the time log below, we can see that step 2 "prescriber number count" took the longest, followed by step 1 “data preparation”.  

To further improve performance when using large datasets, we can find more efficient ways to read in the raw data, and/or to store prescriber information for each drug.  Going forward, we can also try to split large dataset for parallel computing and run the code on environments with better hardware specs.

    - 5 records:
    > Data preparation took 0.0 seconds to run!
    > Prescriber number took 0.0002 seconds to run!
    > Drug cost took 0.0001 seconds to run!
    > Final sorted table took 0.0001 seconds to run!
    > In total pharmacy_counting.py took 0.001 seconds to run!

    - 1k records:
    > Data preparation took 0.0013 seconds to run!
    > Prescriber number took 0.0008 seconds to run!
    > Drug cost took 0.0007 seconds to run!
    > Final sorted table took 0.0005 seconds to run!
    > In total pharmacy_counting.py took 0.0043 seconds to run!


    - 100k records:
    > Data preparation took 0.4207 seconds to run!
    > Prescriber number took 0.6829 seconds to run!
    > Drug cost took 0.1211 seconds to run!
    > Final sorted table took 0.0047 seconds to run!
    > In total pharmacy_counting.py took 1.2345 seconds to run!
