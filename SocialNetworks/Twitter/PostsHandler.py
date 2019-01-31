class PostsHandler:
    @staticmethod
    def get_article_row(url=None, datetime=None, is_retweet=None, comments=None, likes=None, retweets=None, text=None, translation=None):
        """
        Create article-dictionary representation

        :param url: post url
        :param datetime: tweet datetime



        :param comment_on: url original tweet parent tweet

        :param likes: list user profiles ? ['some1', 'some2',...]



        :param retweet: url on original

        :param text: tweet text
        :param text_html: tweet html
        :param translation_en: english translation

        :return: dictionary
        """
        return {
                    "url": url,
                    "date": datetime,
                    "is_retweet": is_retweet,
                    "comments": comments,
                    "likes": likes,
                    "retweets": retweets,
                    "text": text,
                    "translation_en": translation
                }

    @staticmethod
    def parse_posts_list(url_root=None, html=None, acc=None, soup=None):
        """
        Parse list of articles

        :param url_root: server url
        :param html: html to parse
        :param acc: acc to parse
        :param soup: instance of Beautiful Soup
        :return: dictionary{
                             url_1:{
                                    "url": url_1,
                                    "date": date,
                                    "title": title,
                                    "subtitle": subtitle,
                                    "html": None,
                                    "text": None
                                    },
                             url_2:{
                                    ...
                                    }
                                    each row of dictionary could be created by  get_article_row method

        """
        return None

    @staticmethod
    def parse_article_datetime(html=None, soup=None, year=None, month=None, day=None, hour=None, minute=None, second=None):
        """
        Parse article time

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :param day
        :param month
        :param hour
        :param minute
        :param second
        :return: article datetime
        """

        return None

    @staticmethod
    def parse_article_likes(html=None, soup=None):
        """
        Parse article subtitle

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: likes of the post
        """

        return None

    @staticmethod
    def parse_article_comments(html=None, soup=None):
        """
        Parse article subtitle

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: list with comments of the post
        """

        return None

    @staticmethod
    def parse_article_text(html=None, soup=None):
        """
        Parse article text

        :param html: html to parse
        :param soup: instance of Beautiful Soup
        :return: cleaned html (without tag, text only)
        """

        return None
