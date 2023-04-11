 * Code written by [Ali Mohammad Afshari]

My code is a Python script that scrapes Google search suggestions for a list of user inputs and saves the results in an Excel file. The get_questions method in the GoogLe class takes four arguments: question_type, user_input, country_code, and result_count. It returns a list of search suggestions from Google based on the given input.

I define the desktop_path and file_name variables to specify where the output file should be saved. I also define a suggestions_df variable to store the scraped data in a Pandas DataFrame.

Next, the user is prompted to input a comma-separated list of keywords and phrases to search for. I then create a list of Persian letters and iterate over each letter to generate new combinations with the user input. This is done to increase the number of search queries that can be made.

After generating the search queries, my code iterates over them using a loop, calls the get_questions method to scrape Google search suggestions for each query, and appends the results to the suggestions_df DataFrame. The resulting DataFrame is then saved as an Excel file.

Finally, I provide an option for the user to enter additional search terms or exit the program.

Overall, my code makes use of web scraping techniques to gather data from Google search suggestions and stores it in a structured format that can be easily analyzed using Pandas library.
