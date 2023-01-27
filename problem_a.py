import requests


def popular_count():

    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=386ea6e619bc3b5721f33392e34505c2&language=ko-KR&page=1'

    response = requests.get(URL).json()
    popular_movie_list = response['results']

    return len(popular_movie_list)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
