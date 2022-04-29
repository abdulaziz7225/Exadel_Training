# Custom converter from csv to json
def csv_to_json():
    # read the input from file
    with open('my_input.csv', 'r') as file1:
        my_lines = file1.readlines()
        header = my_lines[0].rstrip().split(',')
        len1, len2 = len(header), len(my_lines)
        my_json = []

        for j in range(1, len2):
            my_dict = {}
            my_lines[j] = my_lines[j].rstrip().split(',')
            for i in range(len1):
                my_dict[header[i]] = my_lines[j][i]
            my_json.append(my_dict)

        result = str(my_json).replace("'", '"')

    # write the output to file
    with open('my_output.json', 'w') as file2:
        file2.write(result)


# Custom converter from json to csv
def json_to_csv():
    # open json file
    with open('my_input.json', 'r') as file1:
        my_lines = file1.readlines()

    my_str = ""
    my_list = []
    for i in my_lines:
        my_str += i.strip()

    # Read and convert rows into a list
    number_of_rows = my_str.count('},')
    for _ in range(number_of_rows+1):
        start_index = my_str.find("{")
        end_index = my_str.find("}")
        my_list.append(my_str[start_index: end_index + 1])
        my_str = my_str[:start_index] + my_str[end_index + 1:]

    # Extract header from the json file
    header_list = []
    header_line = my_list[0].split('"')
    for x in range(1, len(header_line), 4):
        header_list.append(header_line[x])
    header = ','.join(header_list)

    # Extract values from the json file
    result = [header]
    for r in range(0, len(my_list)):
        row = my_list[r].split('"')
        row_list = []
        for x in range(3, len(row), 4):
            row_list.append(row[x])
        row = ','.join(row_list)
        result.append(row)

    # write the output to csv file
    with open("my_output.csv", 'w') as file2:
        file2.write("\n".join(result))


csv_to_json()
json_to_csv()
