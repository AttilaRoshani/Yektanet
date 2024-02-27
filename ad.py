from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    a = set()
    def __init__(self, id, title, img_url, link, advertiser):
        if(id in Ad.a):
            print("id is already exists")
            return
        super().__init__()
        self.__id = id
        Ad.a.add(id)
        self.title = title
        self.img_url = img_url
        self.link = link
        self.__advertiser = advertiser
        self.clicks = 0

    def describe_me(self):
        print(f"This is an Ad with title {self.title}")
        

    def get_title(self):
        return self.title
    

    def set_title(self, title):
        self.title = title


    def get_clicks(self):
        return self.clicks
    

    def inc_clicks(self):
        self.clicks+=1


    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser
