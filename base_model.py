class BaseAdvertising:
    def __init__(self):
        self.views = 0
        self.clicks = 0

    def inc_views(self):
        self.views += 1

    def inc_clicks(self):
        self.clicks += 1
    def get_clicks(self):
        return self.clicks

    def describe_me(self):
        print("This is a BaseAdvertising")
