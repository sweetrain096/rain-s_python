import webbrowser
import time
url = "https://www.google.com/search?q="
idol = ["백현", "수지", "아이린"]

for i in idol :
    #openpage = ("{}{}".format(url,i))
    #openpage = (url+i)
    openpage = (f"https://www.google.com/search?q={i}")
    webbrowser.open(openpage)
    time.sleep(1)