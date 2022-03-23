import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = ({'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/90.0.4430.212 Safari/537.36',
'Accept-Language': 'en-US, en;q=0.5'})

def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

def html(url):
    htmldata = getdata(url)
    prasad = BeautifulSoup(htmldata, 'html.parser')
    return (prasad)


url = "https://www.amazon.in/Test-TST_Exclusive1003-Exclusive-1003/dp/B0844592FT?ref_=Oct_DLandingS_D_5ac1e0c0_60&smid=A14CZOWI0VEHLG&th=1"

prasad = html(url)
print(prasad)





import pandas as pd

def get_data(prasad):
    data_str = ""
    cus_list = []
    
    for item in prasad.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list

res = get_data(prasad)
print(res)

data = {'Customer Name': res}
df = pd.DataFrame(data)
df.to_csv('Ouput.csv')
