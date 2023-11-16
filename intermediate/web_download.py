import requests

download_url = input("Paste the link to download: ")
fname = input("What is the file name you want: ")
response = decode(requests.get(download_url))
contents = response.content()

with open(fname, 'wb') as f:
    f.write(contents)
    f.close()
