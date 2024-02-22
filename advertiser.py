from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    total = 0
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.clicks = 0
        self.views = 0

    def describe_me(self):
        print(f"This is an Advertiser with name {self.name}")

    def get_name(self):
        return self.name
    
    def get_clicks(self):
        return self.clicks
    def get_views(self):
        return self.views
    def inc_views(self):
        self.views+=1
    def inc_clicks(self):
        Advertiser.total+=1
        self.clicks+=1
    def set_name(self, name):
        self.name = name
    @staticmethod
    def help():
        return "This class contains information and methods for advertisers."
    def get_total_clicks():
        return Advertiser.total
