import requests
import time
from bs4 import BeautifulSoup


def url_request(url: 'str') -> 'url_response':
    #print('URL: ', url)
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as ex:
        print(f'There was a problem: {ex}')

    return response


def write_to_file(text: 'list') -> 'None':
    with open('composing_programs.txt', 'wb') as f: # TODO: create a filename by parsing the URL given by user in stdin 
        for page in text:
            f.write(bytes(page, 'utf-8'))
            


def get_links(soup: 'BeautifulSoup') -> 'list':
    #print('Soup object: ', soup)
    all_links = set(soup.find_all('a'))
    #print('a tags on page: ', all_links)
    links = []
    for link in all_links:
        if './pages/' in link.get('href'):
            # if statement checks if the link is to a page of the book,
            # if yes, then the '.' is stripped from the beginning, and then the
            # main url to the website is concatenated to the beginning of the link.
            # Then the full link is added to the links list. 
            links.append(url + link.get('href').strip('./'))
            
    
    #print('get_links function: ', links)
    return links


def get_all_text(soup: 'BeautifulSoup') -> 'str':
    text = soup.get_text()
    return text


def parse_html(url: 'str') -> 'None':
    #print('URL request: ', url_request(url).text)
    soup = BeautifulSoup(url_request(url).text, 'html.parser')
    links = get_links(soup)
    print('parse_html: ', links)
    text = []

    # Loop through internal site links to create soup objects for each request response
    soups = []
    for link in links:
        soups.append(BeautifulSoup(url_request(link).text, 'html.parser'))
        print('sleeping')
        time.sleep(1)

    # Loop through list of soup objects and get all text from them
    for soup in soups:
        text.append(get_all_text(soup))

    write_to_file(text)


if __name__ == '__main__':
    url = str(input('Enter a URL: '))
    
    if 'http://' in url or 'https://' in url:
        parse_html(url)

    # while ('http://' not in url) or ('https://' not in url):
    #     url = input('Enter a proper URL: ')
    #     if 'http://' in url or 'https://' in url:
    #         parse_html(url)
        


    
