import requests
from pprint import pprint


def credits(title):

    URL = 'https://api.themoviedb.org/3/search/movie?api_key=386ea6e619bc3b5721f33392e34505c2&language=ko-KR&page=1&include_adult=false&query='+title

    response = requests.get(URL).json()

    if response['results'] == []:
        return None

    else:
        # 검색 결과 중 첫번째 영화의 id로 출연진, 스태프 목록 가져오기
        movie_list = response['results'][0]
        id = movie_list['id']

        URL2 = 'https://api.themoviedb.org/3/movie/' + str(id) + '/credits?api_key=386ea6e619bc3b5721f33392e34505c2&language=ko-KR'

        response2 = requests.get(URL2).json()

        # 조건에 맞는 출연진, 스태프 각각 추출
        people = response2['cast']
        people2 = response2['crew']

        cast_list = []
        crew_list = []

        for i in people:
            if i['cast_id'] < 10 and i['name'] not in cast_list:
                cast_list.append(i['name'])
        
        for i in people2:
            if i['known_for_department'] == 'Directing' and i['name'] not in crew_list:
                crew_list.append(i['name'])

        credits = {}
        credits['cast'] = cast_list
        credits['directing'] = crew_list

        return credits

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
