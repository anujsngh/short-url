from short_url import *


if __name__ == "__main__":
    # test 0
    a = ShortURLService()
    print(a.get_short_url("https://www.google.com/update/new"))

    # test 1
    print(a.get_short_url("https://www.office.microsoft.com/services/powerpoint/create/new_ppt", squish_url=True))

    # test 2
    print(a.get_long_url("https://www.shorturl.com/dyoqrzh"))
