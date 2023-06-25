import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "How can i use scp command to upload file to Server?",
})
print("111")
print(output)