# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import pandas as pd
import logging
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# Create logger object for BeautifulSoup alerts
logger = logging.getLogger("bs4")
logger.setLevel(logging.WARNING)

# Add NullHandler to logger to suppress all messages
handler = logging.NullHandler()
logger.addHandler(handler)


class GoogLe:
    def get_questions(self, question_type, user_input, country_code, result_count):
        question_results = []
        search_query = question_type + " " + user_input + " "
        google_search_url = "http://google.com/complete/search?output=toolbar&gl=" + \
                            country_code + "&q=" + search_query
        result = requests.get(google_search_url)
        soup = BeautifulSoup(result.text, 'lxml')
        for i, suggestion in enumerate(soup.find_all('suggestion')):
            if i >= result_count:
                break
            question = suggestion.get('data')
            question_results.append(question)
        return question_results


desktop_path = 'C:\\Users\\Ali\\Desktop\\keyboard_research_project'
file_name = 'google.xlsx'

# Check if the file has already been created
try:
    # Read the dataframe from the file
    suggestions_df = pd.read_excel(f"{desktop_path}/{file_name}")
except:
    # If the file does not exist, create a new dataframe
    suggestions_df = pd.DataFrame(
        columns=['phrase', 'google suggestions', 'rank'])

input_world = input(
    "Enter a comma separated list of keywords and phrases (or type 'exit' to quit) Keyword Shitter2 : ")
input_world2 = [x.strip() for x in input_world.split("،")]
persian_letters = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ',
                   'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی',
                   'چطور', 'چگونه', 'آیا', 'کجا', 'کدام', 'چرا', 'چه کسی', 'چه زمانی', 'هستند', 'چه']

words_list = []

# The first loop
for letter in persian_letters:
    for word in input_world2:
        new_word = letter + " " + word
        words_list.append(new_word)

# The second loop
for letter in persian_letters:
    for word in input_world2:
        new_word = word + " " + letter
        words_list.append(new_word)

# Remove duplicates
words_list = list(set(words_list))

# Dataframe definition
suggestions_df = pd.DataFrame(columns=['google suggestions', 'phrase'])

# Each word requires 42 counts
count = 0
count_number = len(input_world2)
number_n = 42
final_count = count_number * number_n
while True:
    for user_input in words_list:
        print(f"\033[32msearching in GoogLe '{user_input}'\033[0m")
        q_obj = GoogLe()
        questions = q_obj.get_questions("", user_input, "", 10)

        # Convert the list of suggestions to a DataFrame
        suggestion_results = []

        for i, question in enumerate(questions):
            suggestion_results.append([question, i+1])

        temp_df = pd.DataFrame(suggestion_results, columns=[
                               'google suggestions', 'Rank'])
        temp_df['phrase'] = user_input

        suggestions_df = pd.concat(
            [suggestions_df, temp_df], ignore_index=True)

        count += 1
        if count == final_count:
            break

    if count == final_count:
        break

# Save data frame in excel file

suggestions_df.to_excel('suggestions.xlsx', index=False)

while True:
    # Get input list of words and phrases
    input_list = input(
        u"\033[94mEnter a comma separated list of keywords and phrases (or type 'exit' to quit) GoogLe: \033[0m")

    # Convert Persian input to Unicode (UTF-8)
    input_list = input_list.encode('utf-8').decode('utf-8')

    if input_list.lower() == 'exit':
        # Exit if the user has typed exit
        print("finished.")
        break

    # Separate words and phrases using commas
    user_inputs = [x.strip() for x in input_list.split("،")]

    for user_input in user_inputs:
        print(f"\033[32msearching in GoogLe '{user_input}'\033[0m")
        q_obj = GoogLe()
        questions = q_obj.get_questions("", user_input, "", 10)

        # Convert the list of suggestions to a DataFrame
        suggestion_results = []

        temp_df = pd.DataFrame(suggestion_results)
        suggestions_df = pd.concat(
            [suggestions_df, temp_df], ignore_index=True)

        # Make sure questions, ranks, and user_input lists are the same length
        zipped_lists = [(question, i, user_input)
                        for i, question in enumerate(questions)]
        temp_df = pd.DataFrame(zipped_lists, columns=[
            'google suggestions', 'rank', 'phrase'])

        suggestions_df = pd.concat(
            [suggestions_df, temp_df], ignore_index=True)

    # Save the DataFrame in an Excel file
    suggestions_df.to_excel(f"{desktop_path}/{file_name}", index=False)
