import pyshorteners
url = input("Enter url: \n")

print ("Url after shortening:\n", pyshorteners.Shortener.tinyurl(url))
