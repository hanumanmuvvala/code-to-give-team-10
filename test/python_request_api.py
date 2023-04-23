import requests
import json

filename="C:\\Users\\venub\\OneDrive\\Desktop\\noteworthy-server\\noteworthy-server\\1.mp3"

#headers = {"Content-Type": "audio/mpeg"}

headers = {
    "Content-Type": "application/json"
}

with open(filename, "rb") as f:
    file_data = {"file":f}

create_student = {"student": {"username": "venu",
	"password":"password"
	}}





#response = requests.post("http://127.0.0.1:5000/filelectures", headers=headers,  files=file_data, data = data , timeout = 60)


with open(filename, "rb") as f:
    files = {"file": f}
    data = {
            "user_data": json.dumps(create_student),
            "file_data":files
           }
    response = requests.post("http://127.0.0.1:5000/filelectures", files=files , data = data ,timeout = 60)


print(response.status_code)
print(response.text)