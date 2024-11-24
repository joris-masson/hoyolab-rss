from hoyolab.hoyolabuser import HoyolabUser

if __name__ == '__main__':
    user1 = HoyolabUser(38147774)
    for post in user1.get_last_posts():
        print(post)
