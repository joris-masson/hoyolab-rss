class HoyolabPost:
    def __init__(self, post_link: str, post_title: str, post_content: str):
        self.__post_link: str = post_link
        self.__title: str = post_title
        self.__content: str = post_content
        self.__publish_time: str = ""  # TODO récupérer le temps de publication (sinon le temps de détection)

    def get_post_link(self) -> str:
        return self.__post_link

    def get_title(self) -> str:
        return self.__title

    def get_content(self) -> str:
        return self.__content

    def get_publish_time(self) -> str:
        return self.__publish_time

    def __str__(self):
        return f"{self.__title}: {self.__content}"
