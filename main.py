from base_model import BaseAdvertising
from advertiser import Advertiser
from ad import Ad

if __name__ == "__main__":
    base_advertising = BaseAdvertising()
    advertiser1 = Advertiser(1, "name1")
    advertiser2 = Advertiser(2, "name2")
    ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
    ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)

    base_advertising.describe_me()
    ad2.describe_me()
    advertiser1.describe_me()

    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad1.inc_views()
    ad2.inc_views()

    ad1.inc_clicks()
    ad1.inc_clicks()
    ad1.inc_clicks()
    ad2.inc_clicks()
    ad2.inc_clicks()
    advertiser1.inc_clicks()
    advertiser2.inc_clicks()

    print(advertiser2.get_name())
    advertiser2.set_name("new name")
    print(advertiser2.get_name())

    print(ad1.get_clicks())
    print(advertiser2.get_clicks())
    print(Advertiser.get_total_clicks())
    print(Advertiser.help())
