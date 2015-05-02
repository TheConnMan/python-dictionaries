import csv

def parseLSA():
    header = [];
    LSADict = {};
    with open('data/LSAsamples.csv', 'rb') as csvfile:
        LSAreader = csv.reader(csvfile, delimiter=',');
        for row in LSAreader:
            if len(header) == 0:
                header = [cell.lower() for cell in row];
                for cell in header:
                    if cell != '':
                        LSADict[cell] = {};
            else:
                for i in range(0, len(header)):
                    if header[i] != '' and row[i + 1] != '':
                        LSADict[header[i]][row[i]] = float(row[i + 1]);
                
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
