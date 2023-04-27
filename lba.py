import csv

# Initialize a dictionary to hold the frequency of each LBA
lba_frequency = {}

# Open the CSV file and read its contents
with open('trace/target_MSR_mds_0.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract the LBA value from the row
        lba = row[2]

        # If the LBA value is already in the dictionary, increment its frequency
        if lba in lba_frequency:
            lba_frequency[lba] += 1
        # Otherwise, add the LBA value to the dictionary with a frequency of 1
        else:
            lba_frequency[lba] = 1

# Sort the LBA frequency dictionary by frequency in descending order
sorted_lba_frequency = sorted(lba_frequency.items(), key=lambda x: x[1], reverse=True)

# Write the LBA frequency statistics into a new CSV file
with open('statistic/lba_frequency_statistics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for lba, frequency in sorted_lba_frequency:
        writer.writerow([lba, frequency])
