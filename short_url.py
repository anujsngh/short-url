import string
import random
import re


def extract_domain_url(url):
    """
    URL extractor function to extract domain URL of a given URL.
    """
    # Define a regex pattern to extract the parent URL
    pattern = r'^(https?://[^/]+)'
    
    # Use re.search to find the match
    match = re.search(pattern, url)
    
    # Check if a match was found
    if match:
        domain_url = match.group(1)
        return domain_url
    else:
        return None


def generate_short_url(long_url:str, squish_url=False):
    """
    
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
    domain_url  = extract_domain_url(long_url)

    # Check if squish is true or not.
    if squish_url:
        # Return the mask for long url.
        return "https://www.shorturl.com" + "/" + tiny_str
    else:
        # Return the domain url with random string attached in the end as 
        # mask for long url.
        return domain_url + "/" + tiny_str


if __name__ == "__main__":
    # test 0
    print(generate_short_url("https://www.google.com/update/new"))

    # test 1
    print(generate_short_url("https://www.office.microsoft.com/services/powerpoint/create/new_ppt", squish_url=True))
