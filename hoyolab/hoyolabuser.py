from selenium.webdriver.common.by import By

from hoyolab.hoyolabpost import HoyolabPost
from scrapping.hoyolabscrapper import initialize_driver


class HoyolabUser:
    def __init__(self, user_id: int):
        self.__user_id: int = user_id
        self.__name: str = ""  # TODO récupérer le nom d'utilisateur
        self.__last_posts: list[HoyolabPost] = self.get_last_posts()

    def get_name(self) -> str:
        return self.__name

    def get_url(self):
        return f"https://www.hoyolab.com/accountCenter/postList?id={self.__user_id}"

    def get_last_posts(self) -> list[HoyolabPost]:
        driver = initialize_driver()
        driver.get(self.get_url())

        posts: list[HoyolabPost] = []
        scrapped_posts = driver.find_elements(By.CSS_SELECTOR, ".mhy-article-card__link")
        for post in scrapped_posts:
            link = post.get_attribute("href")
            title = post.find_element(By.CSS_SELECTOR, ".mhy-article-card__text").get_attribute("innerHTML")
            content = post.find_element(By.CSS_SELECTOR, ".mhy-article-card__content").get_attribute("innerHTML")

            posts.append(HoyolabPost(link, title, content))

        driver.quit()

        return posts
