import requests
from pprint import pprint


def recommendation(title):
     
    URL = 'https://api.themoviedb.org/3/search/movie?api_key=386ea6e619bc3b5721f33392e34505c2&language=ko-KR&page=1&include_adult=false&query='+title

    response = requests.get(URL).json()

    if response['results'] == []:
        return None

    else:
        # 검색 결과 중 첫번째 영화의 id로 추천목록 가져오기
        movie_list = response['results'][0]
        id = movie_list['id']
        
        URL2 = 'https://api.themoviedb.org/3/movie/' + str(id) + '/recommendations?api_key=386ea6e619bc3b5721f33392e34505c2&language=ko-KR&page=1'

        response2 = requests.get(URL2).json()
        movie_recommendation = response2['results']

        if movie_recommendation == []:
            return []

        else:
            # 추천목록의 제목만 추출
            recom_title = []
            for i in movie_recommendation:
                recom_title.append(i['title'])
            
            return recom_title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
