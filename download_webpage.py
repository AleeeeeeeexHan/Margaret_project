from urllib.request import urlopen

url  = "https://shopsearch.taobao.com/search?app=shopsearch&q=shoes"

response = urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)
