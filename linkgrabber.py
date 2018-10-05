import linkGrabber

links = linkGrabber.Links(r"http://google.com")
gb = links.find(limit=4,duplicates=False,pretty=True)
print(gb)