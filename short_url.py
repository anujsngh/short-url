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

