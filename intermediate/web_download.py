import requests

download_url = input("Paste the link to download: ")
fname = input("What is the file name you want: ")
response = requests.get(download_url)

with open(fname, 'wb') as f:
    f.write(response.content)
    f.close()
