import requests
from bs4 import BeautifulSoup

def url_request(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as ex:
        print(f'There was a problem: {ex}')
    
    parse_html(response)

    ### writing response to a file ###
    # with open('composing_programs.html', 'wb') as f:
    #     for chunk in response.iter_content(1000):
    #         f.write(chunk)


def get_links(soup):
    all_links = soup.find_all('a')
    urls = []
    for link in all_links:
        urls.append(link.get('href'))
    
    return urls


def parse_html(response):
    soup = BeautifulSoup(response, 'html.parser')
    urls = get_links(soup)
    


if __name__ == '__main__':
    url = ''
    if input():
        url = input()
    
    url_request(url)
