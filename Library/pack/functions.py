import requests
import urllib3
from bs4 import BeautifulSoup
from .constants import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def learnviral(page):
    links_ls = []
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
    }
    
    r = requests.get(LEARNVIR + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    first = soup.find_all('div', class_ = 'content-box')
    soup1 = BeautifulSoup(str(first[1]), 'html.parser')
    title_all = soup1.find_all('h3', class_ = 'entry-title')
    links = soup1.find_all('div', class_ = 'link-holder')

    for index, lk in enumerate(links):
        
        title = title_all[index].text
        links_ls.append(title + '||' + lk.a['href'])
    return links_ls

def real_disc(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
    
    r = requests.get(REALDISC + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    udd = soup.find_all('div', attrs = {'style': 'margin-top:-274px;z-index:9;position: absolute; left: 0; margin-left: 15px; color: #fff; background: rgba(0,0,0,0.5); padding: 2px 4px; font-weight: 700;'})
    content = soup.find_all('div', class_ = 'white-block-content', attrs = {'style': ';background-color: #333333;height: 160px;   overflow: hidden;'})
    # print(len(content))
    # exit()
    for index, i in enumerate(content):
        # print(udd[index].text)
        if udd[index].text.replace('\n', '') == 'Udemy':
            url2 = i.a['href']

            r2 = requests.get(url=url2, headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            title = soup1.find('title').text.replace(' Udemy Coupon - Real Discount', '')
            links_ls.append(title + '||' + soup1.find('div', class_ = 'col-sm-6 col-xs-6 letshover').a['href'])
    return links_ls

def udemy_freebies(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    r = requests.get(UDEMYFREEBIES + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('div', 'theme-block')
    for index, items in enumerate(all):
        title = items.img['title']
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        url3 = soup1.find('a', class_ = 'button-icon')['href']
        link = requests.get(url3, verify=False).url
        links_ls.append(title + '||' + link)
    return links_ls

def udemy_coupons_me(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    r = requests.get(UDEMYCOUPONS + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('div', 'td_module_1 td_module_wrap td-animation-stack')
    if page == 1:
        all = all[2:]
    for index, items in enumerate(all):
        title = items.a['title']
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        try:
            ll = soup1.find('span', class_ = 'td_text_highlight_marker_green td_text_highlight_marker').a['href']
            links_ls.append(title + '||' + ll)
        except:
            ll = ''
    return links_ls

def discudemy(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    r = requests.get(DISCUD + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('section', 'card')
    for index, items in enumerate(all):
        try:
            title = items.a.text
            url2 = items.a['href']
        except:
            title = ''
            url2 = ''
        if url2 != '':
            r2 = requests.get(url2, headers=head, verify=False)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            next = soup1.find('div', 'ui center aligned basic segment')
            url3 = next.a['href']
            r3 = requests.get(url3, headers=head, verify=False)
            soup3 = BeautifulSoup(r3.content, 'html.parser')
            links_ls.append(title + '||' + soup3.find('div', 'ui segment').a['href'])
    return links_ls

def tricksinfo(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    r = requests.get(TRICKSINF + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('a', class_ = 'post-thumb')
    for index, items in enumerate(all):
        title = items['aria-label']
        url2 = items['href']
        r2 = requests.get(url2, headers=head, verify=False)
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('div', 'wp-block-button').a['href']
        links_ls.append(title + '||' + link)
    return links_ls

def freewebcart(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    r = requests.get(WEBCART + str(page), headers=head, verify=False)
    soup = BeautifulSoup(r.content, 'html.parser')
    all = soup.find_all('h2', class_ = 'title')

    
    for index, items in enumerate(all):
        title = items.text
        url2 = items.a['href']
        r2 = requests.get(url2, headers=head, verify=False)
    
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        link = soup1.find('a', class_ = 'btn btn-default btn-lg')['href']
        links_ls.append(title + '||' + link)
    return links_ls

def course_mania(page):
    links_ls = []
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer': 'https://coursemania.xyz/',
        'Origin': 'https://coursemania.xyz',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    
    r = requests.get(COURSEMANIA, headers=head, verify=False)
    js = r.json()
    for items in js:
        title = items['courseName']
        link = items['url']
        links_ls.append(title + '||' + link)
    return links_ls

def comidoc(page):
    
    links_ls = []
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    }

    r = requests.get(COMIDOC, headers=head).json()
    coupons_ls = r['pageProps']['coupons']
    for i in coupons_ls:
        title = i['course']['detail'][0]['title']
        link = 'https://www.udemy.com/course'+ i['course']['cleanUrl'] + '?couponCode=' + str(i['code'])
        links_ls.append(title + '||' + link)
    return links_ls

