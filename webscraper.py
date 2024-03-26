import requests
import os
import sys
from bs4 import BeautifulSoup

# Check if there's at least one argument (script name itself + argument)
if len(sys.argv) < 2:
  print("Please provide a command line argument.")
  sys.exit(1)

# Get the first argument (excluding the script name)
cl_arg_url = sys.argv[1]

# Create a variable using the argument
url = cl_arg_url

print(f"The variable 'url' is now set to: {url}")

# Check if there's at least one argument (script name itself + argument)
if len(sys.argv) < 2:
  print("Please provide a command line argument.")
  sys.exit(2)

# Get the first argument (excluding the script name)
cl_arg_keyword = sys.argv[2]

# Create a variable using the argument
keyword = cl_arg_keyword

print(f"The variable 'keyword' is now set to: {keyword}")


def scrape_website(url, keyword):
  """Scrapes a website for a keyword and returns a list of occurrences.

  Args:
      url: The URL of the website to scrape.
      keyword: The keyword to search for.

  Returns:
      A list of strings containing the occurrences of the keyword.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
  except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the website: {e}")
    return []

  soup = BeautifulSoup(response.content, 'html.parser')
  text = soup.get_text(separator='\n')  # Extract text with newlines as separator
  occurrences = [line for line in text.splitlines() if keyword.lower() in line.lower()]
  return occurrences

# Example usage
#url = "https://www.example.com"  # Replace with the target website
#keyword = "search_term"

results = scrape_website(url, keyword)
def count_occurrences(occurrences):
    word_counts = {}

    for line in results:
    # Split the line into words (case-insensitive)
        words = line.lower().split()
        for word in words:
      # Count occurrences of each word
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

occurrences = ["Found 'search_term' here", "Another 'search_term' occurrence", "This line has 'search_term' twice"]
word_counts = count_occurrences(occurrences)    

print(word_counts)

if results:
  print(f"Found occurrences of '{keyword}':")
  for result in results:
    print(result)
else:
  print(f"Keyword '{keyword}' not found on {url}")
