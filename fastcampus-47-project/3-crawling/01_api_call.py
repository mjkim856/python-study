import requests

url = "https://openapi.naver.com/v1/search/blog.json?query=과천 맛집&start=100&display=5"
res = requests.get(url, headers={"X-Naver-Client-Id": "pNdISaOoIKomHA0fPeSu",
                                 "X-Naver-Client-Secret": "RdzEPmpxS2"})
print(res.json())
r = res.json()

# print(r['items']) << json()은 딕셔너리 형식으로 출력되어서, 이런 식으로 원하는 항목을 확인할 수 있다. 