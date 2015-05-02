import csv

def parseLSA():
    LSADict = {
        'street': {},
        'taxi': {},
        'tongue': {}
    };
    with open('data/LSAsamples.csv', 'rb') as csvfile:
        LSAreader = csv.reader(csvfile, delimiter=',');
        for row in LSAreader:
            if row[1] != '':
                LSADict['street'][row[0]] = row[1];
            if row[4] != '':
                LSADict['taxi'][row[3]] = row[4];
            if row[7] != '':
                LSADict['tongue'][row[6]] = row[7];
                
    return LSADict

LSADict = parseLSA();
print LSADict
