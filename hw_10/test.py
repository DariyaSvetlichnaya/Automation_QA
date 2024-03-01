import csv


def from_csv_to_html(csv_data):
    # Split CSV data into lines
    lines = csv_data.strip().split('\n')

    # Extract column names from the first line
    columns = lines[0].split(',')

    # Initialize the HTML string
    html = ''

    # Iterate over each row starting from the second line
    for line in lines[1:]:
        # Split the row into values
        values = line.split(',')

        # Create HTML tags for each column and concatenate them
        html += ''.join(f"<{column}>{value}</{column}>\n" for column, value in zip(columns, values))

    return html


# Example usage:
csv_data = """name,last_name,age,salary
Leo,Moracchioli,50,5000
Lemmy,Kilmister,83,0"""

html_output = from_csv_to_html(csv_data)
print(html_output)
