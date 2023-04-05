import csv

# define the data
data = [
    ['PlantID', 'PlantName', 'Chairs', 'Tables', 'Couches', 'Recliners'],
    [1001, 'Plant 1', 71, 31, 34, 60],
    [1002, 'Plant 2', 59, 39, 39, 70],
    [1003, 'Plant 3', 97, 20, 58, 69],
    [1004, 'Plant 4', 65, 28, 58, 70],
    [1005, 'Plant 5', 61, 24, 45, 65],
    [1006, 'Plant 6', 52, 37, 38, 64],
    [1007, 'Plant 7', 54, 33, 55, 63],
    [1008, 'Plant 8', 75, 25, 45, 62],
    [1009, 'Plant 9', 56, 27, 51, 63],
    [1010, 'Plant 10', 72, 24, 30, 65],
    [1011, 'Plant 11', 92, 37, 34, 64],
    [1012, 'Plant 12', 80, 26, 54, 64],
    [1013, 'Plant 13', 80, 35, 43, 62],
    [1014, 'Plant 14', 65, 33, 42, 67]
]

# create the file and write the data
with open('plant_production.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# Define the input and output file names
input_file = 'plant_production.csv'
output_file = 'production_summary.csv'

# Initialize the production totals
total_chairs = 0
total_tables = 0
total_couches = 0
total_recliners = 0
num_plants = 0

# Read in the production data from the input file
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    for row in reader:
        num_plants += 1
        total_chairs += int(row[2])
        total_tables += int(row[3])
        total_couches += int(row[4])
        total_recliners += int(row[5])

# Calculate the average production for each type of furniture
avg_chairs = total_chairs / num_plants
avg_tables = total_tables / num_plants
avg_couches = total_couches / num_plants
avg_recliners = total_recliners / num_plants

# Write the summary data to the output file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Furniture', 'Total Production', 'Average Production'])
    writer.writerow(['Chairs', total_chairs, avg_chairs])
    writer.writerow(['Tables', total_tables, avg_tables])
    writer.writerow(['Couches', total_couches, avg_couches])
    writer.writerow(['Recliners', total_recliners, avg_recliners])
