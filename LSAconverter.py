import csv

def parseLSA():
    header = [];
    LSADict = {};
    with open('data/LSA_values.csv', 'rb') as csvfile:                  # Open and read the CSV line by line
        LSAreader = csv.reader(csvfile, delimiter=',');
        for row in LSAreader:
            if len(header) == 0:                                        # If the header hasn't been initialized, initialize it
                header = [cell for cell in row];                # Turn each header element into lowercase
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

#def calculateScore(LSADict, response):
#    LSAKeys = LSADict.keys()
#    score = 0;
#    for key in LSAKeys:                                                 # For each key in the LSA dict
#        if response[key] in LSADict[key]:                               # Check to make sure the reponse value has a score associated with it
#            score += LSADict[key][response[key]];                       # Add the response score to the response's total score
#        else:                                                           # Print an error if a response doesn't have a score
#            print 'ERROR: Response value=' + response[key] + ' doesn\'t exist.'
#    return score;
    
def rewritescores(LSAdict, response):
    LSAKeys = LSADict.keys()
    rewrittenArray = [];
    for key in LSAKeys:                                                 # For each key in the LSA dict
        if response[key] in LSADict[key]:                               # Check to make sure the response value has a score associated with it
            rewrittenArray.append(str(LSADict[key][response[key]]));        # Add the response score to the response's total score
        else:   
            rewrittenArray.append("9999");                                                        # Print an error if a response doesn't have a score
            print 'ERROR: Response value=' + response[key] + ' doesn\'t exist.'
    return rewrittenArray;

LSADict = parseLSA();                                                   # Get the dict
responses = parseResponses('subject_responses1.csv');
with open('data/converted_responses.csv', 'wb') as csvfile:                  # Open and read the CSV line by line
        LSAreader = csv.writer(csvfile, delimiter=',');                  # Parse the responses
        for response in responses:
            array = [response['subject']]
            array.extend(rewritescores(LSADict, response))
            LSAreader.writerow(array)
    #write.writerows
   

