import requests
import json

#headers = {"Content-Type": "application/json"}
filename="C:\\Users\\venub\\OneDrive\\Desktop\\noteworthy-server\\noteworthy-server\\1.mp3"

headers = {"Content-Type": "multipart/form-data", "Content-Disposition": f"attachment; filename={filename}"}
'''
data = {"student": {"username": "venu",
	"password":"password"
	}}


json_data = json.dumps(data)



##Deleting a user
#response = requests.delete("http://127.0.0.1:5000/students/1", headers=headers, data=json_data)

## Creating user
create_student = {"student": {"username": "venu",
	"password":"password"
	}}
response = requests.post("http://127.0.0.1:5000/students", headers=headers, data=json.dumps(create_student))

## Get student usernames
response = requests.get("http://127.0.0.1:5000/usernames", headers=headers, data=json_data)


## Verify student
verify_student = {"student": {"username": "venu",
	"password":"password"
	}}
response = requests.post("http://127.0.0.1:5000/verifystudent", headers=headers, data=json.dumps(verify_student))
url={"url":"https://www.youtube.com/watch?v=_R8bI4ZzSZ8"}
response = requests.post("http://127.0.0.1:5000/summarize", headers=headers, data=json.dumps(url))
'''
'''
files = {"file": open(filename, "rb")}
response = requests.post("http://127.0.0.1:5000/filelectures", files=files, headers=headers,timeout=60)
'''


#filename = "image.jpg"
headers = {"Content-Type": "audio/mpeg"}


with open(filename, "rb") as f:
    files = {"file": f}
    response = requests.post("http://127.0.0.1:5000/filelectures", files=files ,timeout = 60)

print(response.status_code)
print(response.text)