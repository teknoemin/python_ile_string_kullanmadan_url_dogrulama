import re

olanlar = "^(http[s]?:\/\/)?([w]{3}\.)?[a-z0-9\._-]+[.]\w{2,3}([.]\w{2})?$"
def web_adresi_nedir(web):
    if (re.search(olanlar, web)):
    	print("URL formatı doğru!")
    else:
    	print("URL formatı hatalı!")

web_adresi_nedir("www.alierbey.com")