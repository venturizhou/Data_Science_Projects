import pandas as pd
from requests import get
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'ExpiredDate', 'SaleDate',
                           'Views', 'Quanity', 'Price', 'Condition', 'Title', 'Description', 'Damage', 'Sold'])


def grab_info(URL, df):
    page = get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    temp = dict.fromkeys(['Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'SaleDate',
                          'Views', 'Quanity', 'Price', 'Condition', 'Title', 'Description', 'Damage', 'Sold'])

    for k in temp.keys():
        try:
            temp[k] = soup.find('span', string=k).find_next_sibling(
                'span').text.strip('\n\t')
        except AttributeError:
            temp[k] = None

    temp['Price'] = soup.select(
        'div[class*="listing_price"]')[0].find('span').text
    temp['ListDate'] = soup.find('span', string='Listed').find_next_sibling(
        'span').text.strip('\n\t')
    temp['ExpiredDate'] = soup.find('span', string='Expires').find_next_sibling(
        'span').text.strip('\n\t')
    temp['Quantity'] = soup.find(
        'span', string='Quantity Available').find_next_sibling('span').text.strip('\n\t')
    temp['Description'] = soup.find('div', attrs={'class': 'desc_block'}).text
    temp['Condition'] = soup.find('span', attrs={'class': 'speclabel'}).text
    if temp['Condition'] != 'Mint':
        temp['Damage'] = soup.find(
            'div', attrs={'class': 'desc_block'}).find_next_sibling('div').text
    temp['Title'] = soup.find(
        'div', attrs={'class': 'col-xs-12 col-md-8'}).find_next('h3').text
    df.loc[URL[-9::]] = temp

    # attributes=soup.find_all('div', attrs = {'class': 'listing_attr'})
    # description=soup.find_all('div', attrs = {'class': 'desc_block'})[
    #     0].text.strip('\n')
    # try:
    #     damage = soup.find_all('div', attrs={'class': 'desc_block'})[
    #     1].text.strip('\n')
    # except IndexError:
    #     damage = "NaN"

    # lst = [attribute.find(
    #     'span', attrs={'class': 'value'}).text for attribute in attributes]
    # lst = list(map(lambda x: ''.join(char for char in x if char.isalnum()), lst))
    # lst.append(description)
    # lst.append(damage)
    # if soup.select('div[class*="disabled"]'):
    #     lst.append('Yes')
    # else:
    #     lst.append('No')
    # df.loc[URL[-9::]]=lst

# def grab_info(URL, df):
#     page = get(URL)
#     soup = BeautifulSoup(page.content, 'lxml')
#     temp = dict.fromkeys(['Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'SaleDate',
#                            'Views', 'Quanity', 'Price', 'Condition', 'Description', 'Damage', 'Sold'])

#     temp['Price'] = soup.select('div[class*="listing_price"]')[0].find('span').text

#     attributes = soup.find_all('div', attrs={'class': 'listing_attr'})
#     temp['Condition'] = soup.find('span', attrs={'class': 'speclabel'}).text
#     description = soup.find_all('div', attrs={'class': 'desc_block'})[
#         0].text.strip('\n')
#     try:
#         damage = soup.find_all('div', attrs={'class': 'desc_block'})[
#         1].text.strip('\n')
#     except IndexError:
#         damage = "NaN"

#     lst = [attribute.find(
#         'span', attrs={'class': 'value'}).text for attribute in attributes]
#     lst = list(map(lambda x: ''.join(char for char in x if char.isalnum()), lst))
#     lst.append(description)
#     lst.append(damage)
#     if soup.select('div[class*="disabled"]'):
#         lst.append('Yes')
#     else:
#         lst.append('No')
#     df.loc[URL[-9::]] = lst


grab_info('https://swappa.com/listing/view/LUJT81025', df)
print(df)
