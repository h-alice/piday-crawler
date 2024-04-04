import requests
import sys

AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def get_page(page_number):
    """ Fetch a page from the million pi API """

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

def pi_pretty_print(current_buffer, pi_digits: str, counter=-2, group_size=5, newline_group=10, output_limit=-1, with_line_digit_counter=False):
    """ Pretty print the digits of pi.  

    Returns:
        buffer (str): The pretty printed digits of pi.
        counter (int): The number of current digits after the decimal point.
    """

    output_buffer = current_buffer

    # The -2 of counter is to skip the "3." part.
    current_digit_counter = counter

    for digit in pi_digits:

        if output_limit > 0 and current_digit_counter >= output_limit: # Stop if the output limit is set and reached.
            break

        if current_digit_counter <= 0: # Skip the "3.", just added to the buffer.
            output_buffer += digit     # Add digit to the buffer. 
            current_digit_counter += 1 # Increment counter.
        else:
            if current_digit_counter % group_size == 0: # Add a space every `group_size` digits.
                output_buffer += " " # Add a space., after digit group.
            output_buffer += digit
            current_digit_counter += 1
        
        if current_digit_counter % group_size == 0:  # Invoke only when the current digit is a multiple of `group_size`.
            current_group = current_digit_counter // group_size
            if current_group == 0: # Skip the first group. (the '3.' part)
                continue
            elif (current_digit_counter // group_size) % newline_group == 0: # Add a newline every `newline_group` groups.
                if with_line_digit_counter:
                    output_buffer += f"  <{current_digit_counter}>" # Add the current digit counter to the buffer, before newline.
                output_buffer += "\n "

    return output_buffer, current_digit_counter

if __name__ == "__main__":

    if len(sys.argv) > 1:
        max_digit = int(sys.argv[1])
    else:
        print("Usage: python crawler.py <max_digit>")
        print("Outputs the first <max_digit> digits of pi after the decimal point.")
    
    buf = ""

    # The count represents the number of digits "after" the decimal point.
    # Therefore, the initial value is -2 to skip the "3." part.
    counter = -2 
    page_counter = 1
    while counter < max_digit:
        data = get_page(page_counter)
        buf, counter = pi_pretty_print(buf, data, counter=counter, group_size=5, newline_group=10, output_limit=max_digit, with_line_digit_counter=True)
        page_counter += 1

    print(buf)

    