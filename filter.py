import json

def get_answers(packet: str):
    dic = json.loads(packet)
    dic = dic['data']['problems']
    ans = []
    for p in dic:
        if p['content']['Type'] == 'SingleChoice':
            ans += [chr(ord('A') + p['content']['answerIndex'])]
        else:
            ans += ['X']
    return ans

if __name__ == "__main__":
    with open("packet.json", "r", encoding='ascii') as f:
        print(get_answers(f.read()))