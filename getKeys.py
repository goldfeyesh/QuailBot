# get the token or API key

def getKeyFromFile(filename):
    searchAPIKeyFile = open('nullKeyFile.txt', 'r')
    if filename == 'searchAPIKey.txt':
        searchAPIKeyFile = open(filename, 'r')
    elif filename == 'token.txt':
        searchAPIKeyFile = open(filename, 'r')
    return searchAPIKeyFile.readline().strip()
