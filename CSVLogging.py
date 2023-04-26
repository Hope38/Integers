import csv
import logging

# Configure logging
logging.basicConfig(filename='egg_production.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_csv(file_name):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['House', 'Number_Of_Eggs'])
            writer.writerow(['House_1', 1002])
            writer.writerow(['House_2', 1210])
            writer.writerow(['House_3,'])
            writer.writerow(['House_4',1410])
            writer.writerow(['House_5',1121])
            # Add more rows as needed
        logging.info(f'CSV file created: {file_name}')
    except Exception as e:
        logging.critical(f'Error creating CSV file: {e}')

# Function to read CSV file
def read_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError as e:
        logging.critical(f'CSV file not found: {e}')
        return None
    except Exception as e:
        logging.critical(f'Error reading CSV file: {e}')
        return None

# Function to calculate total production
def calculate_total_production(data):
    total_production = 0
    for row in data:
        if 'Number_Of_Eggs' in row and row['Number_Of_Eggs'].isdigit():
            total_production += int(row['Number_Of_Eggs'])
        else:
            logging.warning(f'No production number found for house: {row["House"]}')
    return total_production

# Function to calculate average production per house
def calculate_average_production(data):
    total_production = calculate_total_production(data)
    num_houses = len(data)
    average_production = total_production / num_houses if num_houses > 0 else 0
    return average_production

# Function to write summary CSV file
def write_csv(file_name, data):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        logging.critical(f'Error writing summary CSV file: {e}')

# Main program
def main():
    logging.info('Program started')
    file_name = 'egg_production.csv'
    create_csv(file_name) # Call create_csv function with file_name as argument
    data = read_csv(file_name)
    if data is not None:
        total_production = calculate_total_production(data)
        average_production = calculate_average_production(data)
        summary_data = [{'Total_Production': total_production, 'Average_Production_Per_House': average_production}]
        write_csv('egg_production_summary.csv', summary_data)
        logging.info('Summary data written to egg_production_summary.csv')
    logging.info('Program finished')

if __name__ == '__main__':
    main()

