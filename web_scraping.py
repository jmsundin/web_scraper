import requests
from bs4 import BeautifulSoup


def url_request(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as ex:
        print(f'There was a problem: {ex}')

    return response


def write_to_file(text):
    "Writing text to a file"
    with open('composing_programs.txt', 'wb') as f: # TODO: create a filename by parsing the URL given by user in stdin 
        for page in text:
            f.write(page)


def get_links(soup):
    all_links = soup.find_all('a')
    urls = []
    for link in all_links:
        urls.append(link.get('href'))
    
    return urls


def get_all_text(soup):
    text = soup.get_text()
    return text


def parse_html(response):
    soup = BeautifulSoup(response, 'html.parser')
    urls = get_links(soup)
    text = []

    # Loop through internal site links to create soup objects for each request response
    soups = []
    for url in urls:
        soups.append(BeautifulSoup(url_request(url), 'html.parser'))

    # Loop through list of soup objects and get all text from them
    for soup in soups:
        text.append(get_all_text(soup))

    write_to_file(text)


if __name__ == '__main__':
    url = ''
    if input():
        url = input()
    
    response = url_request(url)

    # uncomment line below if you want the response to be written to a file
    #write_to_file(response)

    parse_html(response)
