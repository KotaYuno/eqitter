import requests
import json

def api(sentence):

    url = "https://labs.goo.ne.jp/api/morph"

    payroad = {"app_id":"b2a00b62e6ad775c1c61dca424b63dc352291fd09948b3a172136edf5ca82dfa", "request_id":"record001", "sentence":sentence, "info_filter":"form"}

    print(payroad)
    result = requests.post(url, json.dumps(payroad), headers={'Content-Type': 'application/json'})
    print(result.text)

if __name__ == "__main__":
    api("私の名前は竹内です。")
