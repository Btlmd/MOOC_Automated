import json

def get_answer_post(text: str):
    dic = json.loads(text)
    print(dic['data']['description'])
    dic = dic['data']['problems']
    ans = []
    for p in dic:
        ans += [''.join(sorted(p['user']['answer']))]
    print(ans)

if __name__ == "__main__":
    with open("export.json", "r") as f:
        lst = f.readlines()
        for l in lst:
            get_answer_post(l)