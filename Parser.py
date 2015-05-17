import csv

def parseLSA():
    header = [];
    LSADict = {};
    with open('data/LSAsamples.csv', 'rb') as csvfile:                  # Open and read the CSV line by line
        LSAreader = csv.reader(csvfile, delimiter=',');
        for row in LSAreader:
            if len(header) == 0:                                        # If the header hasn't been initialized, initialize it
                header = [cell.lower() for cell in row];                # Turn each header element into lowercase
                for cell in header:
                    if cell != '':                                      # If a cell isn't blank add it as a key to the dict
                        LSADict[cell] = {};                             # Result: LSADict = {'street': {}, 'taxi': {}, 'tongue': {}}
            else:
                for i in range(0, len(LSADict.keys())):                 # Start adding values to dict
                    if row[3 * i + 1] != '':                            # If value exists (because some columns are shorter than others)
                        score = float(row[3 * i + 1]);                  # Convert the score to a float
                        LSADict[header[3 * i]][row[3 * i]] = score;     # Add the score to the dict (e.g. LSADict['street']['bike'] = 0.3)
    return LSADict

def parseResponses(fileName):
    header = [];
    responseList = [];
    with open('data/' + fileName, 'rb') as csvfile:
        responseReader = csv.reader(csvfile, delimiter=',');
        for row in responseReader:
            if len(header) == 0:                                        # If the header hasn't been initialized, initialize it
                header = row;                                           # Just set the header to be the header row
            else:
                response = getResponseObject(header, row);              # Get the response object
                responseList.append(response);                          # Add it to the response list
    return responseList;

def getResponseObject(header, row):
    response = {};                                                      # Initialize the response dict
    for i in range(0, len(row)):                                        # For each column
        response[header[i]] = row[i];                                   # Add the value to the response dict under the header key
    return response;

def rewriteScores(LSADict, response):
    LSAKeys = LSADict.keys()
    rewrittenString = '';
    for key in LSAKeys:                                                 # For each key in the LSA dict
        if response[key] in LSADict[key]:                               # Check to make sure the reponse value has a score associated with it
            rewrittenString += ',' + str(LSADict[key][response[key]])   # Add the response score to the rewritten string
        else:                                                           # Print an error if a response doesn't have a score
            rewrittenString += ',0.0'; 
            print 'ERROR: Response value=' + response[key] + ' doesn\'t exist.'
    return rewrittenString;

LSADict = parseLSA();                                                   # Get the dict
responses = parseResponses('responsefilesample.csv');                   # Parse the responses
for response in responses:
    print response['subject'] + rewriteScores(LSADict, response);
