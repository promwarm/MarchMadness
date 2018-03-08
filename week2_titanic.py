# https://www.reddit.com/r/PythonProjects2/comments/82v68j/march_madness_managing_big_data/

# Version 1, without looking at examples
import requests
from  bs4 import BeautifulSoup

url = 'http://www.titanicfacts.net/titanic-passenger-list.html'

class Passenger:

    def __init__(self, name, type_of_class, age, status):
        self.name = name
        self.type_of_class = type_of_class
        self.age=age
        self.status = status

# Connect to a certain URL
def connect_url (url, response, **kwargs):
    user_agent= 'python-requests/4.8.2 (Compatible; A. Wallet; mailto: aris.wallet@gmail.com)'

    if kwargs:
        user_agent = 'python-request/4.8.2 (compatible, {}, mailto:{})'.format(kwargs['name'], kwargs['email'])

    cns_rsps=requests.get(url, headers={'User-Agent': user_agent}, timeout=10)
    if response: print("Status code {} returned for url: {}".format(cns_rsps.status_code,url))
    print ('')
    return cns_rsps

first_class = []
second_class = []
third_class = []

response = connect_url(url, True)
soup = BeautifulSoup(response.content, 'html.parser')

iteration = 0
tables=soup.find_all('table', limit=3)
for table in tables:
    iteration += 1 # 1 = 1st class, 2 = 2nd class, 3 = 3rd class
    rownumber = 0
    for row in table.findAll('tr'):
        rownumber += 1
        if rownumber == 1:
            continue # skip headers

        cells = row.findAll('td')
        surname = cells[0].find(text=True)
        name = cells[1].find(text=True)
        age = cells[2].find(text=True)
        boarded = cells[3].find(text=True)
        status = cells[4].find(text=True)

        complete_name=surname # Maybe I want to add surname later
        person = Passenger(complete_name, iteration, age, status)
        if iteration == 1:
            first_class.append(person)
        elif iteration == 2:
            second_class.append(person)
        else:
            third_class.append(person)

print('There were {} passengers in first class, {} passenger in second class and {} passengers in third class.'.format(len(first_class),len(second_class),len(third_class)))

