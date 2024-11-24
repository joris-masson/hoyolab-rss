class HoyolabPost:
    def __init__(self, post_link: str, post_title: str, post_content: str):
        self.__post_link: str = post_link
        self.__title: str = post_title
        self.__content: str = post_content
        self.__publish_time: str

    def __str__(self):
        return f"{self.__title}: {self.__content}"
