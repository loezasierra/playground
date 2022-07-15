# Twitter Username Script
# Usage: python usernames.py <words.txt>

import sys
import os.path
import requests
import json
from config import config

## Constants ##
class constants:
    # Info from: https://developer.twitter.com/en/docs/twitter-api/rate-limits
    RATE = 300        # Request limit
    RATE_WINDOW = 900 # 15 minutes

    # Info from https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by
    URL_NAME_LIMIT = 99 

    # Token
    BEARER_TOKEN = config.BEARER_TOKEN

    # Files
    OUTFILE = "available.txt"
    API_LOG = "api_log.txt"

## Functions ##

"""
None -> String or False
Return the valid name of a .txt file from argument
        False if file is invalid
"""
def get_file():
    usage = "Usage: python usernames.py <words.txt>"

    # Check valid usage
    if len(sys.argv) != 2:
        print(usage)
        return False
    
    input = sys.argv[1]

    # Check valid file type
    if not input.endswith(".txt"):
        print("Invald file type")
        print(usage)
        return False

    # Check file exists
    if not os.path.exists(input):
        print("File does not exist")
        print(usage)
        return False
    
    # Check file is not empty
    if not os.path.getsize(input) > 0:
        print("File is empty")
        print(usage)
    
    return input


"""
String -> [listof String]
Return a list of words separated by \n from a .txt file
"""
def get_words(file):
    with open(file, "r") as f:
        words = f.read().splitlines()
    return words


"""
Method required by bearer token authentication
"""
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {constants.BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


"""
[listof String] -> [listof String]
Return a list of usernames available to register on Twitter using twitter API
"""
def filter_usernames(words):
    names = []

    # Split words into lists that URL can handle
    limit = constants.URL_NAME_LIMIT
    split = [(words[i:i+limit]) for i in range(0, len(words), limit)]

    for words in split:
        # Format usernames
        # Last word added separately to avoid adding a trailing comma
        usernames = "usernames="
        for w in words[:-1]:
            usernames += f"{w},"
        usernames += words[-1]

        # Format url
        url = f"https://api.twitter.com/2/users/by?{usernames}"

        # Connect to endpoint
        response = requests.request("GET", url, auth=bearer_oauth,)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
    
        # Get list of names that returned errors
        json_response = response.json()
        try:
            errors = json_response["errors"]
        except:
            continue

        # Log for debugging
        log_data(
            constants.API_LOG,
            json.dumps(json_response, indent=4, sort_keys=True)
        )

        # Add to list of names that don't exist
        for e in errors:
            if e["title"] == "Not Found Error":
                names.append(e["value"])
    return names


"""
String String -> None
Write given data to a log file for debugging purposes
"""
def log_data(file, data):
    with open(file, "a") as f:
        f.write(data)
    return


"""
[listof String] String -> None
Output a list of usernames separated by \n to a .txt file 
"""
def output_usernames(names, file):
    with open(file, 'w') as f:
        for n in names:
            f.write(n)
            f.write('\n')
    return


"""
.txt file -> .txt file
Filter a text file of words to only those available as twitter usernames
"""
def main():
    # Get file
    infile = get_file()
    if not infile:
        return

    words = get_words(infile)
    available = filter_usernames(words)
    output_usernames(available, constants.OUTFILE)
    return



# Run main
if __name__ == "__main__":
    main()
