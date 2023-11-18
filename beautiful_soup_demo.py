# example of reading the lists from the HTML document 
from bs4 import BeautifulSoup

# Read in the HTML document
with open('example.html', 'r') as file:
    html = file.read()
print ('String ===> \n' , html, '\n <====== String ')

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
print ('Parsed Tree ===> \n' , soup, '\n <====== Parsed Tree  ')

# Find all the links in the unordered list
links = soup.find('ul').find_all('a')
print('Links received ', links)
# Print the links
for link in links:
    print(link.contents[0] , ' : ', link['href'])

# example of Finding elements by tag name < text > 
from bs4 import BeautifulSoup

# Read in the HTML document
with open('example.html', 'r') as file:
    html = file.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find all the paragraphs in the document
paragraphs = soup.find_all('p')

# Print the text of each paragraph
for paragraph in paragraphs:
    print(paragraph.text)


# Example of Finding elements by CSS selector

from bs4 import BeautifulSoup

# Read in the HTML document
with open('example.html', 'r') as file:
    html = file.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Find all the links in the document
links = soup.select('a')
# links = soup.find_all('a') # same as select above 
print(links)
# Print the text and href attributes of each link
for link in links:
    print(link.text, link['href'])


# Modifying the HTML

from bs4 import BeautifulSoup

# Read in the HTML document
with open('example.html', 'r') as file:
    html = file.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Change the text of the h1 element
soup.h1.string = 'New Page Title'

# Add a new paragraph to the document
new_paragraph = soup.new_tag('p')
new_paragraph.string = 'This is a new paragraph.'
soup.body.append(new_paragraph)

# Save the modified HTML to a file
with open('modified.html', 'w') as file:
    file.write(str(soup))

