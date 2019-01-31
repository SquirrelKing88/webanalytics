class Scraper:
    @staticmethod
    def getPostId(post):
        return post.id

    @staticmethod
    def getPostDate(post):
        return post.date

    @staticmethod
    def getPostMessage(post):
        return post.message

    @staticmethod
    def getPostForwardedFrom(post):
        if post.fwd_from:
            return post.fwd_from.channel_id
        return None

    @staticmethod
    def getPostMedia(post):
        #TODO if it is in need
        return None

    @staticmethod
    def getPostViews(post):
        return post.views

    @staticmethod
    def getPostEditDate(post):
        if not post.edit_date:
            return None
        return post.edit_date.strftime("%d/%m/%Y %H:%M:%S")