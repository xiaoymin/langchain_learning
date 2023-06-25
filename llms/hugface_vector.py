import requests

API_URL = "https://api-inference.huggingface.co/models/GanymedeNil/text2vec-large-chinese"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": {
		"source_sentence": "That is a happy person",
		"sentences": [
			"That is a happy dog",
			"That is a very happy person",
			"Today is a sunny day"
		]
	},
})

print(output)