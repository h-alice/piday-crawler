# Pi Day Crawler for 1M Digits of Pi

# Introduction
This is a simple crawler script that fetches the first 1M digits of Pi from the website [piday.org](http://www.piday.org/million/). The crawler is written in Python and uses the `requests` library to fetch the webpage and equipped with a pretty-printer to display the digits in a more readable format.

# Requirements
- Python 3.x (Written and tested on Python 3.11)
- requests library (install using `pip install requests`)

# How to Use
1. Clone the repository or download the `crawler.py` file.
2. Install the `requests` if you haven't already.
    ```bash
    pip install requests
    ```
3. Run the script! Or use `--help` flag to see the available options.
    ```bash
    python crawler.py
    ```

# Sample Output
```bash
$ python crawler.py 100

3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510
  58209 74944 59230 78164 06286 20899 86280 34825 34211 70679
```