import json
import re


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
