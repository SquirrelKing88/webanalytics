class CommonPostsHandler:
    @staticmethod
    def get_post_row(url=None, date=None, likes=None, reposts=None, comments=None, html=None, text=None, translation_en=None, own_post=True):
        """
        Create article-dictionary representation

        :param url: post url
        :param date: publication time
        :param likes: post likes
        :param reposts: post reposts
        :param comments: post comments
        :param html: html
        :param text: cleared text
        :param translation_en: english translation
        :param own_post: True - own post, False - repost
        :return: dictionary
        """
        return {
                    "url": url,
                    "date": date,
                    "likes": likes,
                    "reposts": reposts,
                    "comments": comments,
                    "own_post":own_post,
                    "text": text,
                    "html": html,
                    "translation_en": translation_en
                }

    @staticmethod
    def parse_post_list(url_root=None, html=None, soup=None):
        """
        Parse list of posts

        :param url_root: server url
        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: dictionary

        """
        return None

    @staticmethod
    def parse_post_datetime(html=None, soup=None, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        """
        Parse post time

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :param day
        :param month
        :param hours
        :param minutes
        :param seconds
        :return: post datetime
        """

        return None

    @staticmethod
    def parse_post_likes(html=None, soup=None):
        """
        Parse post likes

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: likes of post
        """

        return None

    @staticmethod
    def parse_post_reposts(html=None, soup=None):
        """
        Parse post reposts

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: reposts of post
        """

        return None

    @staticmethod
    def parse_post_comments(html=None, soup=None):
        """
        Parse post comments

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: coments of post
        """

        return None

    @staticmethod
    def parse_post_text(html=None, soup=None):
        """
        Parse post text

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: html, cleaned html (without tag, text only)
        """

        return None, None



