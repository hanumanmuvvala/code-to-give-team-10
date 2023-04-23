import requests

url = 'http://localhost:5000/openChat'
#url = 'http://localhost:5000/summary'

'''
data = {
    'name': 'First Lecture',
    'filename': '1.mp3',
'isurl':"False",
'creator':2,
'language':'English'
}

'''
data = {
'user_name':'hanuman',
'user_role' :'wish_maker'
}


'''
files = {
    'file': open('C:\\Users\\venub\\OneDrive\\Desktop\\noteworthy-server\\noteworthy-server\\1.mp3', 'rb')
}

'''
#response = requests.post(url, data=data, files=files)
response = requests.get(url, data=data)

print(response.status_code)
print(response.text)




