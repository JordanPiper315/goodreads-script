import urllib.request
from bs4 import BeautifulSoup
import csv

filename = "goodreads_library_export.csv"

def main():
  fields = []
  rows = []
  with open(filename, 'r') as csvfile:
      csvreader = csv.reader(csvfile)
      fields = next(csvreader)
      for row in csvreader:
          #rows.append(row)
          if row[18] == "to-read":
            title = row[1]
            author = row[2]
            librarySearch(title, author)

# make function for call to library search
def librarySearch(title, author):
    if title.find(' '):
       title = title.replace(' ', '%20')
    if author.find(' '):
       author = author.replace(' ', '%20')
    # print(title, author)
    url = f"https://libcat.co.humboldt.ca.us/search~S13/X?SEARCH=t:({title})%20and%20a:({author})&searchscope=13&SORT=D"
    try:
      request = urllib.request.Request(url)
      content = urllib.request.urlopen(request)
      soup = BeautifulSoup(content, 'html.parser')
      author_chunk = soup.find("td", class_="bibInfoData").text
      title_chunk = soup.find("td", string="Title").next_sibling.next_sibling.text
      location_chunk = soup.find("tr", class_="bibItemsEntry").text
      writeToFile(author_chunk, title_chunk, location_chunk)
    except Exception as e:
      print('Error')
      
def writeToFile(author, title, location):
   lines = [author, title, location]
   with open('libraryBooks.txt', 'a') as f:
    # f.write(title, author)
    for line in lines:
        f.write(line)
        f.write('\n')
   
if __name__ == "__main__":
   main()

# read csv file, for every book check if in humboldt library, if true input into text file
