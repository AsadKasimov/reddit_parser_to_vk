from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def write_In_file(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url=url)
    time.sleep(3)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, -1000);")

    with open("html_files/ht.html", "w", encoding='UTF-8') as file:
        file.write(driver.page_source)
    driver.close()
    driver.quit()


def get_page():
    with open("html_files/ht.html", encoding="utf8") as file:
        # читает ранее записанный код
        src = file.read()
    # используем lxml т.к. он быстрее парсит
    soup = BeautifulSoup(src, "lxml")

    all_news_part = soup.find("div", class_="rpBJOHq2PR60pnwJlUyP0")
    with open("html_files/poisk.html", 'w', encoding='UTF-8') as f:
        f.write(str(all_news_part))
    news_dict = {}
    news_time = {}
    news_content = {}
    news_picture = {}
    num = 1
    nu = 1
    co = 1
    pi = 1
    for news in all_news_part:
        # извлекам url из постов с url
        for link in news.find_all('a', class_="styled-outbound-link"):
            t = link.get("href")
            news_dict[num] = t
            num += 1
        # извлекам время
        date = news.find_all('span', class_="_2VF2J19pUIMSLJFky-7PEI")
        for d in date:
            time = d.get_text(strip=True)
            news_time[nu] = time
            nu += 1
        # извлекаем новость
        content = news.find_all('h3', class_="_eYtD2XCVieq6emjKBH3m")
        for c in content:
            s = c.get_text(strip=True)
            news_content[co] = s
            co += 1
        img = news.find_all('img',
                            class_="_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax")
        for i in img:
            pic = i.get('src')
            news_picture[pi] = pic
            pi += 1
    print(news_dict)
    print(news_time)
    print(news_content)
    print(news_picture)

        #with open("txt_files/parsing_result.txt", 'w', encoding='UTF-8') as f:






def main():
    write_In_file("https://www.reddit.com/r/animenews/?f=flair_name%3A%22New%20Releases%22")
    get_page()


if __name__ == "__main__":
    main()
