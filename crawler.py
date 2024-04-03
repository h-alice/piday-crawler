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

def pi_pretty_print(pi_digits: str, counter=-2, group_size=5, newline_group=10, output_limit=-1):
    """ Pretty print the digits of pi """
    # The -2 of counter is to skip the "3." part
    output_buffer = ""

    current_digit_counter = counter

    for digit in pi_digits:

        if output_limit > 0 and current_digit_counter >= output_limit: # Stop if the output limit is set and reached.
            break

        if current_digit_counter <= 0: # Skip the "3.", just added to the buffer.
            output_buffer += digit
            current_digit_counter += 1
        else:
            if current_digit_counter % group_size == 0: # Add a space every `group_size` digits.
                output_buffer += " "
            output_buffer += digit
            current_digit_counter += 1
        
        if current_digit_counter % group_size == 0:  # Invoke only when the current digit is a multiple of `group_size`.
            current_group = current_digit_counter // group_size
            if current_group == 0: # Skip the first group. (the '3.' part)
                continue
            elif (current_digit_counter // group_size) % newline_group == 0: # Add a newline every `newline_group` groups.
                output_buffer += "\n "

    return output_buffer, current_digit_counter





if __name__ == "__main__":
    page_number = 1
    data = get_page(page_number)
    data_1 = data[:1002]
    data_2 = data[1002:2000]

    data, counter = pi_pretty_print(data_1, counter=-2, group_size=5, newline_group=10)
    print(data, counter)

    