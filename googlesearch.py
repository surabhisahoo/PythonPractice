import webbrowser

new = 2
url = r"http://google.com/?#q="
search_string = input(" Enter String to search: ")
webbrowser.open(url + search_string,new = new)