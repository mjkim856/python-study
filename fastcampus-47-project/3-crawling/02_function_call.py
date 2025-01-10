import requests

def call_api(keyword, start, display):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": "pNdISaOoIKomHA0fPeSu",
                                    "X-Naver-Client-Secret": "RdzEPmpxS2"})
    print(res)
    r = res.json()
    return r

if __name__ == '__main__':      # import 가능하도록 main 사용
    r = call_api("정부과천청사역", 1, 2)
    for item in r['items']:
        print(item)
        print()