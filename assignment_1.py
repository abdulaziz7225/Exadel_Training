import json


# Custom converter from csv to json
def json_to_csv():
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
def csv_to_json():
    # read the input from file
    with open("my_input.json", "r") as file1:
        my_list = json.load(file1)
        my_list2 = []
        my_list2.append(",".join(my_list[0].keys()))
        for i in my_list:
            my_list2.append(",".join(i.values()))
        result = "\n".join(my_list2)

    # write the output to file
    with open('my_output.csv', 'w') as file2:
        file2.write(result)


json_to_csv()
csv_to_json()
