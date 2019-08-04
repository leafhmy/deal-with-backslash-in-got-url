#图片
#"small_image":"\/\/a.vpimg3.com\/upload\/merchandise\/pdcvis\/612187\/2019\/0723\/101\/e8bd1220-1d36-4bdb-9f52-629a55a16512_420_531.jpg","countryFlag
#通过循环替换更改后的列表中的元素
import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for j in range(1,21):
    url="https://category.vip.com/suggest.php?keyword=%E9%AB%98%E8%B7%9F%E5%87%89%E9%9E%8B&page="+str(j)
    try:
        data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        pat = 'small_image":"....(.*?)","countryFlag'#不完全图片网址
        result = re.compile(pat).findall(data)
        #print(len(result))
        for i in range(0,len(result)):
            for h in range(0,len(result)):
                a = result[h]
                b = a.replace("\\","")
                result[h] = b
            imgurl = "http://"+result[i]#构造完整图片网址
            file = "D:/Test/PIC/"+str(j)+"-"+str(i)+".jpg"#存放目录
            urllib.request.urlretrieve(imgurl, filename=file)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    except Exception as e:
        print(e)
