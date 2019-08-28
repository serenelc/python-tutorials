import csv
import json

if __name__ == '__main__':
    with open('MOCK_DATA.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        headers = True
        contacts = []
        for line in csv_reader:
            if headers is True:
                header_names = line
                headers = False
                continue
            else:
                contacts.append(dict(zip(header_names, line)))

        print(json.dumps(contacts, indent=3))