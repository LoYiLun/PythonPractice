#藉由首頁取得所有文章的URL
import requests
from bs4 import BeautifulSoup
import json

test = open("spider/pet/test.txt","w",encoding='UTF-8')
print("此為Dcard圖片爬蟲\n請輸入要爬熱門文章或者最新文章(熱門輸入1，否則輸入2)")
number = int(input())

print("請輸入要爬幾篇文章")
number2 = int(input())
p = requests.Session()
if number == 1:
    url=requests.get("https://www.dcard.tw/f/sex")
elif number ==2:
    url=requests.get("https://www.dcard.tw/f/sex?latest=true")
soup = BeautifulSoup(url.text,"html.parser")
sel = soup.select("div.PostList_entry_1rq5Lf a.PostEntry_root_V6g0rd")
a=[]

for s in sel:
    a.append(s["href"])
url = "https://www.dcard.tw"+ a[2]

for k in range(0,10):
        post_data={
            "before":a[-1][9:18],
            "limit":"30",
            "popular":"true"
        }
        r = p.get("https://www.dcard.tw/_api/forums/sex/posts",params=post_data, headers = { "Referer": "https://www.dcard.tw/", "User-Agent": "Mozilla/5.0" })
        data2 = json.loads(r.text)
        for u in range(len(data2)):
            Temporary_url = "/f/sex/p/"+ str(data2[u]["id"]) + "-" + str(data2[u]["title"].replace(" ","-"))
            a.append(Temporary_url)
j=0 #為了印頁數
q=0 #為了印張數
for i in a[1:number2+1]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    #file.write("temperature is {} wet is {}%\n".format(temperature, humidity))
    test.write("第 {} 頁的URL為: {} \n".format(j,url))
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_jpg = soup.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")
    for c in sel_jpg:
        q+=1
        print("第",q,"張:",c["src"])
        test.write("%\n""第 {} 張: {} \n".format(q,c["src"])) 
        pic=requests.get(c["src"])
        img2 = pic.content
        pic_out = open("spider/pet/"+str(q)+".png",'wb')
        pic_out.write(img2)
        pic_out.close()

test.close()
print("爬蟲結束")