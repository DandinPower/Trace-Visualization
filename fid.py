import csv

# Initialize a dictionary to hold the frequency of each fid
fid_frequency = {}

# Open the CSV file and read its contents
with open('trace/target_MSR_mds_0.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        # Extract the fid value from the row
        fid = row[1]

        # If the fid value is already in the dictionary, increment its frequency
        if fid in fid_frequency:
            fid_frequency[fid] += 1
        # Otherwise, add the fid value to the dictionary with a frequency of 1
        else:
            fid_frequency[fid] = 1

# Sort the fid frequency dictionary by frequency in descending order
sorted_fid_frequency = sorted(fid_frequency.items(), key=lambda x: x[1], reverse=True)

# Write the fid frequency statistics into a new CSV file
with open('statistic/fid_frequency_statistics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for fid, frequency in sorted_fid_frequency:
        writer.writerow([fid, frequency])