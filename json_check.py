import json

def search_word(word):
    json_file = open("./db/seword.json", 'r',encoding="utf-8")
    json_load = json.load(json_file)
    try:
        return json_load[word]
    except:
        return "None"

def insert_word(word,pro=None,mean=None,ex=None,cate=None):
    json_file = open("./db/seword.json", 'r',encoding="utf-8")
    json_load = json.load(json_file)
    data = []
    if word in json_load.keys():
        for tmp_data in json_load[word]:
            data.append(tmp_data)
    new_data = {
        "pronounce": pro,
        "mean": mean,
        "example": ex,
        "category": cate
        }
    data.append(new_data)
    json_load[word] = data
    print(data)
    with open('./db/seword.json', 'w') as f:
        json.dump(json_load, f, indent=4)

if __name__ == "__main__":
    insert_word('投げる')
    search_word('投げる')


