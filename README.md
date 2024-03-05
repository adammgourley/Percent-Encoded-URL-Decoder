# URL Decoder

CLI tool to decode a given URL or a list of URLs in a given file. Written in Python.

### Examples
``` zsh
# Supply a file that contains many URLs, one on each line
python3 decode.py --file="./urls.txt"

# Supply a singular URL to decode
python3 decode.py --url="https://google.com/%24"

# Supply a file, and write output to a file rather than std out
python3 decode.py --file="./urls.txt" --output="./output.txt"
```