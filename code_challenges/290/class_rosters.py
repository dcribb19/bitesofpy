import csv

YEAR = '2020'


def class_rosters(input_file):
    ''' Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted.'''
    roster = []
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row == '':
                continue
            id, _, classes = row[0], row[1], row[2:]
            classes = [course.split()[0] for course in classes if course != '']
            for cl in classes:
                roster.append(f'{cl},{YEAR},{id}')

    return roster
