import json
import re
import random
import string


def generate_long_url(short_url:str):
    urls = load_from_json(file_name="short_to_long.json")

    if urls:
        if short_url in urls:
            return urls[short_url]
    
    return None


def generate_short_url(long_url:str, squish_url=False):
    """
    Function to create short url from long url.
    """

    urls = load_from_json(file_name="long_to_short.json")

    if urls:
        if long_url in urls:
            return urls[long_url]
    
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
        short_url =  "https://www.shorturl.com" + "/" + short_str
    else:
        # Return the domain url with random string attached in the end as 
        # mask for long url.
        short_url =  domain_url + "/" + short_str

    urls = load_from_json(file_name="short_to_long.json")
    if urls:
        if short_url in urls:
            return short_url
    
    # Saving  The short_url -> long_url and long_url -> short_url 
    # for future references.
    save_short_to_long_url(short_url, long_url)
    save_long_to_short_url(short_url, long_url)

    return short_url
    


def save_short_to_long_url(short_url, long_url):
    urls = load_from_json(file_name="short_to_long.json")

    if urls is None:
        urls = {
            short_url: long_url
        }
        save_to_json(data=urls, file_name="short_to_long.json")
    else:
        if short_url not in urls:
            urls[short_url] = long_url
            save_to_json(data=urls, file_name="short_to_long.json")


def save_long_to_short_url(short_url, long_url):
    urls = load_from_json(file_name="long_to_short.json")

    if urls is None:
        urls = {
            long_url: short_url
        }
        save_to_json(data=urls, file_name="long_to_short.json")
    else:
        if long_url not in urls:
            urls[long_url] = short_url
            save_to_json(data=urls, file_name="long_to_short.json")



def extract_domain_url(url):
    """
    URL extractor function to extract domain URL of a given URL using regex.
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


def save_to_json(data:dict, file_name:str):
    # Convert the dictionary to a JSON-formatted string
    json_string = json.dumps(data, indent=4, sort_keys=True)

    # Save the JSON-formatted string to a file
    with open(file_name, "w") as json_file:
        json_file.write(json_string)


def load_from_json(file_name: str):
    try:
        # Open the JSON file in read mode
        with open(file_name, "r") as json_file:
            # Use json.load() to parse the JSON data into a dictionary
            data = json.load(json_file)

        # Now, 'data' contains the dictionary read from the JSON file
        return data
    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except json.JSONDecodeError as e:
        # Handle the case when the file contains invalid JSON
        print(f"Error: Unable to decode JSON in '{file_name}': {e}")
        return None
