from urllib.request  import urlopen
with urlopen('http://www.baidu.com/') as f:
    print(f.read(300))