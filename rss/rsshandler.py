import xml.etree.cElementTree as ET

from hoyolab.hoyolabpost import HoyolabPost


class RSSHandler:
    def __init__(self, channel_name: str, channel_description: str, channel_link: str):
        self.__channel_name: str = channel_name
        self.__channel_description: str = channel_description
        self.__channel_link: str = channel_link

        self.__root: ET.Element = ET.Element("rss", {"version": "2.0"})
        self.__channel: ET.Element = self.initialize_channel()

    def initialize_channel(self) -> ET.Element:
        channel = ET.SubElement(self.__root, "channel")

        ET.SubElement(channel, "title").text = self.__channel_name
        ET.SubElement(channel, "description").text = self.__channel_description
        ET.SubElement(channel, "link").text = self.__channel_link

        return channel

    def add_post(self, post: HoyolabPost) -> ET.Element:
        item = ET.SubElement(self.__channel, "item")

        ET.SubElement(item, "title").text = post.get_title()
        ET.SubElement(item, "description").text = post.get_content()
        ET.SubElement(item, "pubDate").text = post.get_publish_time()
        ET.SubElement(item, "link").text = post.get_post_link()

        return item

    def write_rss(self):
        tree = ET.ElementTree(self.__root)
        tree.write("rss_feed.xml")
