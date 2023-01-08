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
#url1 = input("Enter the URL of the first webpage: ")
#url2 = input("Enter the URL of the second webpage: ")
#url3 = input("Enter the URL of the third webpage: ")
url1 = 'https://www.itecco.co.uk/job/graduate-software-engineer-6?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'
url2 = 'https://www.brightnetwork.co.uk/graduate-jobs/starling-bank/graduate-software-engineer-london-2023?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'
url3 = 'https://www.totaljobs.com/job/graduate-software-developer/spectrum-it-recruitment-south-ltd-job99529127?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'


# Count the words on each webpage
word_counts1 = count_words(url1)
word_counts2 = count_words(url2)
word_counts3 = count_words(url3)

# Create a table to display the results
table = PrettyTable()
table.field_names = ["Word", "Frequency"]

# Add the results for the first webpage to the table
for word, count in word_counts1.items():
    table.add_row([word, count])

# Add the results for the second webpage to the table
for word, count in word_counts2.items():
    table.add_row([word, count])

# Add the results for the third webpage to the table
for word, count in word_counts3.items():
    table.add_row([word, count])

# Display the table
table.sortby = "Frequency"
table.reversesort = True
print(table)




# Example URLs:
# 'https://www.itecco.co.uk/job/graduate-software-engineer-6?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic',
# 'https://www.brightnetwork.co.uk/graduate-jobs/starling-bank/graduate-software-engineer-london-2023?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic',
# 'https://www.totaljobs.com/job/graduate-software-developer/spectrum-it-recruitment-south-ltd-job99529127?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic'
