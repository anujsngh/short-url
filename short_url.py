import string
import random
import utils


class ShortURLService():
    def __init__(self) -> None:
        pass

    def get_short_url(self, long_url:str, squish_url=False):
        return utils.generate_short_url(long_url, squish_url)
    
    def get_long_url(self, short_url:str):
        return utils.generate_long_url(short_url)



if __name__ == "__main__":
    # test 0
    a = ShortURLService()
    print(a.get_short_url("https://www.google.com/update/new"))

    # test 1
    print(a.get_short_url("https://www.office.microsoft.com/services/powerpoint/create/new_ppt", squish_url=True))

    # test 2
    print(a.get_long_url("https://www.shorturl.com/dyoqrzh"))

