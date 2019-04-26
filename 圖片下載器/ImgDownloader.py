import requests
import urllib.request
from  bs4 import BeautifulSoup
import os
import time

print('input keyword')
keyword = str(input())
url = 'https://www.google.com.tw/search?hl=zh-TW&authuser=0&biw=1366&bih=625&tbm=isch&sa=1&ei=En7CXOf5L9CNr7wPkPC5mAU&q='  + keyword + '&oq='+ keyword +'&gs_l=img.3..0l10.11401.12033..12274...0.0..0.47.168.4......1....1..gws-wiz-img.......35i39.2bj1tJK3tq0'
#url = 'https://www.flickr.com/search/?text=' + keyword
photolimit = 10



headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url,headers = headers) #使用header避免訪問受到限制

soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('img')

folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

    os.makedirs(folder_path) #Create folder



for index , item in enumerate (items):

    if (item and index < photolimit ):

        html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request

        img_name = folder_path + str(index + 1) + '.png'



        with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

            file.write(html.content)

            file.flush()

        file.close() #close file

        print('第 %d 張' % (index + 1))

        time.sleep(1)



print('Done')