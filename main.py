import requests
import bs4

def main():
    for i in range(1,26):
        print(i, end=',')
        resp = requests.get('https://adventofcode.com/2023/leaderboard/day/'+str(i))
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        res = soup.find_all('main')        
        res2 = res[0].find_all('div')
        print(res2[-1].find_all('span')[1].text)

if __name__ == '__main__':
    main()

