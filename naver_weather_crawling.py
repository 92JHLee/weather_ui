from bs4 import BeautifulSoup
import requests


# weather_area = input('날씨를 알고 싶은 지역을 입력하세요: ')
print('***** 오늘의 날씨 정보*******')
weather_area =input('지역을 입력하세요. > ')

weather_html = requests.get(f'https://search.naver.com/search.naver?query={weather_area}날씨') #구월동날씨 검색

# print(weather_html) # 200 응답코드 확인

weather_soup  =BeautifulSoup(weather_html.text,'html.parser') #weather_html을 html로 잘라라! 파싱한 응답결과 html

# print(weather_soup)

try:
    area_title = weather_soup.find('h2', {'class':'title'}).text #text는 태그를 제외한 것만 뽑아줌, 위치 뽑아줌
    today_temper = weather_soup.find('div', {'class':'temperature_text'}).text #현재 온도 뽑아줌
    today_temper = today_temper[6:9]
    yesterday_weather = weather_soup.find('p',{'class':'summary'}).text
    yesterday_weather = yesterday_weather[0:13]

    today_weather = weather_soup.find('span',{'class':'weather before_slash'}).text
    today_rain = weather_soup.find('dd',{'class':'desc'}).text
    weather_list = weather_soup.select('dl.summary_list>dd') # 리스트로 출력됨
    humidity = weather_list[1]
    wind = weather_list[2]

    dust_info = weather_soup.find_all('span',{'class':'txt'})
    dust1 = dust_info[0].text #미세먼지
    dust2 = dust_info[1].text #초미세먼지

except:
    try:
        #해외 도시 검색시 크롤링될 태그 정의
        area_title = weather_soup.find('span',{'class':'btn_select'}).text #날씨를 검색한 지역명 크롤링
        area_title = area_title.strip()
        today_temper = weather_soup.find('span', {'class':'todaytemp'}).text
        today_temper=f"{today_temper}°"
        today_weather = weather_soup.find('p', {'class': 'cast_txt'}).text
        yesterday_weather = '-'
        today_rain = '-'
        humidity = '-'
        wind = '-'
        dust1 = '-'
        dust2 = '-'
    except:
        area_title = '검색한 지역은 날씨 정보가 없습니다.'
        today_temper ='-'
        yesterday_weather = '-'
        today_rain = '-'
        today_weather='-'
        humidity ='-'
        wind = '-'
        dust1 = '-'
        dust2 = '-'


print('지역 : '+area_title)
print('기온 : '+today_temper)
print(yesterday_weather)
print('강수확률 : ' + today_rain)
print('날씨 : '+today_weather)
print('습도 : ' +humidity)
print('풍속 : '+wind)
print('미세먼지 : '+dust1)
print('초미세먼지 : '+dust2)
# print(weather_list)