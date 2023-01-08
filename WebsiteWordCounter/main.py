import requests
from bs4 import BeautifulSoup
from collections import Counter
from prettytable import PrettyTable

def count_words(url):
    # Scrape the webpage
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get all the text from the webpage
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    return word_counts

# Ask the user for the URLs of the webpages
urls = []
url = input("Enter the URL of a webpage (enter 'done' when finished): ")
while url != 'done':
    urls.append(url)
    url = input("Enter the URL of a webpage (enter 'done' when finished): ")

# Count the words on each webpage
word_counts_list = []
for url in urls:
    word_counts = count_words(url)
    word_counts_list.append(word_counts)

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Word", "Frequency"]

# Add the results for each webpage to the table
for word_counts in word_counts_list:
    for word, count in word_counts.items():
        table.add_row([word, count])

# Display the table
table.sortby = "Frequency"
table.reversesort = True
print(table)





# Example URLs:
# 'https://www.itecco.co.uk/job/graduate-software-engineer-6?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic',
# 'https://www.brightnetwork.co.uk/graduate-jobs/starling-bank/graduate-software-engineer-london-2023?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic',
# 'https://www.totaljobs.com/job/graduate-software-developer/spectrum-it-recruitment-south-ltd-job99529127?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'
