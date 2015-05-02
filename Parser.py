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
                LSADict['street'][row[0]] = float(row[1]);
            if row[4] != '':
                LSADict['taxi'][row[3]] = float(row[4]);
            if row[7] != '':
                LSADict['tongue'][row[6]] = float(row[7]);
                
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

def calculateScore(LSADict, response):
    LSAKeys = LSADict.keys()
    score = 0;
    for key in LSAKeys:
        if response[key] in LSADict[key]:
            score += LSADict[key][response[key]];
        else:
            print 'ERROR: Response value=' + response[key] + ' doesn\'t exist.'
    return score;

LSADict = parseLSA();
responses = parseResponses('responsefilesample.csv');
for response in responses:
    score = calculateScore(LSADict, response);
    print 'Score for subject *' + response['subject'] + '* is ' + str(score)
