import requests


entrypoint_sample = "https://www.piday.org/wp-json/millionpi/v1/million?action=example_ajax_request&page=3"

AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def get_page(page_number):
    entrypoint = "https://www.piday.org/wp-json/millionpi/v1/million"
    payload = {
        "action": "example_ajax_request",
        "page": page_number
    }
    response = requests.get(entrypoint, params=payload, headers={"User-Agent": AGENT})

    if response.status_code != 200:
        raise ValueError("Failed to fetch page: %s" % response.status_code)
    elif response.text == "":
        raise StopIteration("Empty page, stopping.")
    
    return response.json()

if __name__ == "__main__":
    page_number = 1
    data = get_page(page_number)
    print(data)
    print(len(data))