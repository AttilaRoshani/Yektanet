class BaseAdvertising:
    def __init__(self):
        self.__views = 0
        self.__clicks = 0

    def inc_views(self):
        self.__views += 1

    def inc_clicks(self):
        self.__clicks += 1
    def get_clicks(self):
        return self.__clicks

    def describe_me(self):
        print("This is a BaseAdvertising")
