from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__()
        self.id = id
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser

    def describe_me(self):
        print(f"This is an Ad with title {self.title}")
        

    def get_title(self):
        return self.title
    

    def set_title(self, title):
        self.title = title


    def get_clicks(self):
        return self.clicks
    

    def inc_clicks(self):
        self.advertiser.inc_clicks()
        self.clicks+=1


    def set_advertiser(self, advertiser):
        self.advertiser = advertiser
