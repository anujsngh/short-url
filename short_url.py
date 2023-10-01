import string
import random
import utils


def generate_short_url(long_url:str, squish_url=False):
    """
    Function to create short url from long url.
    """
    # Generate a random integer value between 6 to 10 
    # to decide length  of random string.
    str_len = random.randint(6, 10)

    # Generate list of all the alphabets in lowercase.
    lower_chars = string.ascii_lowercase

    # Select characters randomely and join chars till 
    # defined length is achieved.
    short_str = "".join([random.choice(lower_chars) for _ in range(str_len)])

    # Extract domain url from the long url.
    domain_url  = utils.extract_domain_url(long_url)

    # Check if squish is true or not.
    if squish_url:
        # Return the mask for long url.
        short_url =  "https://www.shorturl.com" + "/" + short_str
    else:
        # Return the domain url with random string attached in the end as 
        # mask for long url.
        short_url =  domain_url + "/" + short_str

    save_short_to_long_url(short_url, long_url)
    save_long_to_short_url(short_url, long_url)

    return short_url
    

def save_short_to_long_url(short_url, long_url):
    urls = utils.load_from_json(file_name="short_to_long.json")

    if urls is None:
        urls = {
            short_url: long_url
        }
        utils.save_to_json(data=urls, file_name="short_to_long.json")
    else:
        if short_url not in urls:
            urls[short_url] = long_url
            utils.save_to_json(data=urls, file_name="short_to_long.json")


def save_long_to_short_url(short_url, long_url):
    urls = utils.load_from_json(file_name="long_to_short.json")

    if urls is None:
        urls = {
            long_url: short_url
        }
        utils.save_to_json(data=urls, file_name="long_to_short.json")
    else:
        if long_url not in urls:
            urls[long_url] = short_url
            utils.save_to_json(data=urls, file_name="long_to_short.json")


if __name__ == "__main__":
    # test 0
    print(generate_short_url("https://www.google.com/update/new"))

    # test 1
    print(generate_short_url("https://www.office.microsoft.com/services/powerpoint/create/new_ppt", squish_url=True))
