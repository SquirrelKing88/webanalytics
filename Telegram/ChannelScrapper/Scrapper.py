class Scrapper:
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
        return post.fwd_from

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