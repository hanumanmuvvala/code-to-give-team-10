import requests

url = 'http://localhost:5000/filelectures'


data = {
    'name': 'First Lecture',
    'file_name': '5.mp3',
'isurl':"True",
'creator':2,
'language':'English'
}


files = {
    'file': open('"C:\\Users\\venub\\OneDrive\\Desktop\\noteworthy-server\\noteworthy-server\\1.mp3"', 'rb')
}



response = requests.post(url, data=data, files=files)
#response =requests.post(url, data=data)

print(response.status_code)
print(response.text)




