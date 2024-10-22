"""
1. Below is a database diagram

Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points

"""

print("################Question 1################")

import requests

offset = 0
limit = 100
url = "https://api.jolpi.ca/ergast/f1/2020/results/"

# Fetch the data
results_data = []
while True:
    response = requests.get(url, params={'limit': limit, 'offset': offset})
    if response.status_code == 200:
        # Converting the response to json
        results_data = results_data + (response.json()['MRData']['RaceTable']['Races'])
        offset = offset + 100
        if offset > 300:
            break
        break  # we can remove this break for all results for now lets use the first 100 data

    else:
        print(f"Failed to retrieve data: {response.status_code}")
        results_data = []
        break


def query_2020_results(race_data):
    race_results = []
    # Collecting data from each race entry
    for race_entry in race_data:
        location = race_entry['Circuit']['Location']['locality']
        race_name = race_entry['raceName']
        season = race_entry['season']
        race_date = race_entry['date']

        for result in race_entry['Results']:
            driver_name = result['Driver']['givenName'] + " " + result['Driver']['familyName']
            constructor_name = result['Constructor']['name']
            points = float(result['points'])  # float value will be good for sorting
            grid = result['grid']
            position = result['position']
            fastest_lap = result.get('FastestLap', {}).get('lap', 'N/A')
            time = result.get('Time', {}).get('time', 'N/A')  # Default is NA

            # lets append all the   relevant information into the race_results list
            race_results.append({
                'location': location,
                'grid': grid,
                'position': position,
                'fastest_lap': fastest_lap,
                'points': points,
                'driver_name': driver_name,
                'race_name': race_name,
                'time': time,
                'team_name': constructor_name,
                'date': race_date,
                'season': season
            })

    # Sorting the gotten  results by points in descending order
    results_sorted = sorted(race_results, key=lambda x: x['points'], reverse=True)

    # Printing data as a table
    print(
        f"{'Location':<15}{'Grid':<5}{'Position':<10}{'Fastest Lap':<12}{'Points':<8}{'Driver':<25}{'Race_name':<30}{'Time':<15}{'year':<15}{'team_name':<20}{'Date':<10}")
    print("-" * 140)
    for entry in results_sorted:
        print(
            f"{entry['location']:<15}{entry['grid']:<5}{entry['position']:<10}{entry['fastest_lap']:<12}{entry['points']:<8}{entry['driver_name']:<25}{entry['race_name']:<30}{entry['time']:<15}{entry['season']:<15}{entry['team_name']:<20}{entry['date']:<10}")


#Testing the function if it works

query_2020_results(results_data)


""" 2. Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"""


def check_if_palindrome(original_phrase):
    """ Removing the space in between and making sure that the word will be in lower case
        for uniformity in both forward and reverse
    """
    lowercase_unspaced_phrase = original_phrase.replace(" ", "").lower()

    # Reversing lowercase_unspaced_phrase the word to be compared with original word
    reversed_word = lowercase_unspaced_phrase[::-1]

    # Compare the reversed word to check if it matches with the original word
    if reversed_word == original_phrase:
        return f'The Phrase {original_phrase} is a palindrome'
    else:
        return f'The Phrase {original_phrase} is NOT a palindrome'


print("################Question 2################")

user_input = input(f"Enter Phrase To Test: default:madam : ")

# Return the user's input if provided, otherwise return the default value
if user_input == "":
    word_to_check = "madam"
else:
    word_to_check = user_input

print(check_if_palindrome(word_to_check))  # True

"""3. Write a Python function to check whether a string is pangram or not. (Assume 
the string passed in does not have any punctuation)
Note: Pang rams are words or sentences containing every letter of the 
alphabet at least once. For example: "The quick brown fox jumps over the 
lazy dog"""


def check_if_pangram(string_to_test):
    #  Converting the passed sentence to lowercase so that we can reduce computation with lower and upper
    lowercase_string = string_to_test.lower()

    # defining all letters of the alphabet in lower case
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # Removing all the spaces so that we can check if all alphabets will be a set of the string
    all_letters_in_string = set(lowercase_string.replace(" ", ""))

    #  Check if all alphabet letters are in the string
    if alphabet.issubset(all_letters_in_string):
        return "This String is Pangram"
    else:
        return "This String is NOT a Pangram"


print("################Question 3################")

user_input = input(f"Enter String To Check: default:The quick brown fox jumps over the lazy dog : ")

# Return the user's input if provided, otherwise return the default value
if user_input == "":
    string_to_check = "The quick brown fox jumps over the lazy dog"
else:
    string_to_check = user_input
print(check_if_pangram(string_to_check))



"""
3. Write a program that takes an integer as input and returns an integer with 
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19
"""


def reverse_integer(number_to_reverse):
    # it is easier to reverse a number if we convert it to string first
    string_to_reverse = str(number_to_reverse)

    if number_to_reverse < 0:
        # if number is negative we shall reverse the string after the sign
        reversed_str = "-" + string_to_reverse[:0:-1]
    else:
        # For positive numbers, will just reverse the digits
        reversed_str = string_to_reverse[::-1]

    # Convert the reversed string back to an integer
    return int(reversed_str)


print("################Question 4################")
user_input = input(f"Enter Integer To Reverse: default: -56 : ")

# Return the user's input if provided, otherwise return the default value
if user_input == "":
    number_to_reverse = -56
else:
    number_to_reverse = user_input

print(reverse_integer(number_to_reverse))

"""
5. Write a program that accepts a string as input, capitalizes the first letter of each 
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"

"""


def capitalize_the_words(input_string):
    # Creating words in an array so we can loop each word capitalizing each letter
    words = input_string.split()
    capitalized_words = []
    # loop for words so that in the arrays
    for word in words:
        # Check if the word is not empty
        if len(word) > 0:
            # Capitalizing the first letter and make the rest lowercase
            capitalized_word = word[0].upper() + word[
                                                 1:].lower()
            capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)


print("################Question 5################")

user_input = input(f"Enter String To Capitalize: default:i love programming : ")


if user_input == "":
    string_to_capitalize = "i love programming"
else:
    string_to_capitalize = user_input

print(capitalize_the_words(string_to_capitalize))
