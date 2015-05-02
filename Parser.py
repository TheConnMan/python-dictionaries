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

def parseResponses(fileName):
    header = [];
    responseList = [];
    with open('data/' + fileName, 'rb') as csvfile:
        responseReader = csv.reader(csvfile, delimiter=',');
        for row in responseReader:
            if len(header) == 0:
                header = row;
            else:
                response = getResponseObject(header, row);
                responseList.append(response);
    return responseList;

def getResponseObject(header, row):
    response = {};
    for i in range(0, len(row)):
        response[header[i]] = row[i];
    return response;

LSADict = parseLSA();
responses = parseResponses('responsefilesample.csv');
print LSADict
print responses
