import json


def read_json(jsonfile, comment='//'):
    """
    Read a JSON file that contains comments. Contents of the file are returned
    as a dictionary. Commented lines in the JSON file are ignored.
    """

    json_str = ''

    with open(jsonfile, 'r') as json_file:
        for line in json_file:
            if comment not in line:
                json_str += line

    json_dict = json.loads(json_str)
    return json_dict


if __name__ == '__main__':
    file = 'example.json'
    jsondict = read_json(file)

    print('--- jsondict ---')
    print(jsondict)

    print('--- items from jsondict ---')
    print('name', jsondict[1]['first_name'])
    print('last id', jsondict[-1]['id'])
