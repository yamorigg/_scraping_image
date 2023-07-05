import random
import string
import requests
import uuid
import sys
from multiprocessing import Pool

sys.setrecursionlimit(10000)

# 再帰による実装
def get_imgur_url(length: int, start: str = None) -> str:
    if length <= 0:  # エラー処理
        return ''

    buffer = random.choice(string.ascii_letters + string.digits)
    buffer = start + buffer if start else buffer

    if length <= 1:  # 再帰の末尾
        return 'https://i.imgur.com/' + buffer + random.choice(['.png', '.png'])

    return get_imgur_url(length-1, buffer)


# これも再帰
def get_imgur_random(count: int):
    print(1)
    if count <= 0:
        # 再帰の末尾
        return
    # url_lengh = random.randint(5, 7)
    # url = get_imgur_url(url_lengh)
    url = get_imgur_url(6)
    ext = url.split('.')[-1].rstrip('/')  # 拡張子
    resp = requests.get(url, allow_redirects=False)  # 画像の取得


    # if resp.history:  # historyが存在すればリダイレクトされてるってこと
    #     return get_imgur_random(count)

    if resp.status_code == 302:
        # print(resp.status_code)
        # print("url:", url)
        # return
        return get_imgur_random(count)


    binary = resp.content
    resp.close()

    print("Success", url)

    with open(f'./imgur_images/{uuid.uuid4()}.{ext}', 'wb') as f:
        f.write(binary)

    return get_imgur_random(count - 1)  # 再帰

argList = [300, 300, 300, 300, 300, 300, 300]

if __name__ == '__main__':
    p = Pool(6)
    p.map(get_imgur_random, argList)
    # get_imgur_random(2000)

