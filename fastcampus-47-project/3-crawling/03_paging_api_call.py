import requests

def call_api(keyword, start, display):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": "pNdISaOoIKomHA0fPeSu",
                                    "X-Naver-Client-Secret": "RdzEPmpxS2"})
    r = res.json()
    return r

def get_paging_call(keyword, quantity):
    repeat = quantity // 100 # 1000총 10번
    result = []
    for i in range(repeat):
        start = i * 100 + 1
        # 101
        if start > 1000:
            start = 1000
        print(f"{i + 1}번 반복 합니다. start:{start}")
        r = call_api(keyword, start=start, display=100)
        print(r['items'][0])
        result += r['items']
    return result

if __name__ == '__main__':      # import 가능하도록 main 사용
    r = get_paging_call("과천역 맛집", 1100)
    print()
    print(r[0])
    print()
    print(len(r))