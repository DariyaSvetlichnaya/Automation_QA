import json


# Function to read data from the json file
def read_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


# Function to write data to a new file
def write_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Function to update salaries based on conditions
def update_salaries(data):
    for department in data['departments']:
        expenses = department['expenses']
        income = department['income']
        if expenses < income:
            for employee in department['employees']:
                employee['salary'] = round(employee['salary'] * 1.1, 2)
    return data


# Main function
def main():
    input_file = 'departments.json'
    output_file = 'new_costs.json'

    # Read data from the input file
    data = read_data(input_file)

    # Update salaries based on conditions
    updated_data = update_salaries(data)

    # Write updated data to the output file
    write_data(updated_data, output_file)

    print(f"Updated data has been written to {output_file}")


if __name__ == "__main__":
    main()
