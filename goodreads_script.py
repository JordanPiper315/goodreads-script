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
            #print(row)
  print("Field names are:" + ", ".join(field for field in fields))


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
      parse = BeautifulSoup(content, 'html.parser')
      span_elems = parse.find_all("span", attrs={"style": "color:RED"})
      print(span_elems)
      headings = []
      #elems = parse.table.table.table.table.find_all("span") # don't really need author and title name, can just get it from original input
      title = title.replace('%20', ' ')
      author = author.replace('%20', ' ')
      #writeToFile(title, author)
      #for e in elems:
      #print(elems)
      # table_date = table.find_all("tr")
      # data = []
      # for td in table_date.find_all("td"):
      #    headings.append(td.b.text.replace("\n", '').strip())

      # author = parse.table.text.strip().replace('\n', ',')
      # title = parse.table.text.strip().replace('\n', ',')
      # writeToFile(text1)
      #print(author, title)
    except Exception as e:
      print('Error')
      
def writeToFile(title, author):
   lines = [title, author]
   with open('libraryBooks.txt', 'a') as f:
    # f.write(title, author)
    for line in lines:
        f.write(line)
        f.write('\n')
   
if __name__ == "__main__":
   main()

# read csv file, for every book check if in humboldt library, if true input into text file
