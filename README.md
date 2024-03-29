# Percent-Encoded URL Decoder

CLI tool to decode a given URL or a list of URLs in a given file. Written in Python.

For example, if you had a URL like so, *[https://example.com/search?q=hello%20world&lang=en%2Fus]()*
which contains percent encoded characters, %2F and %20, you can use this tool to decode the URL to
*[https://example.com/search?q=hello world&lang=en/us]()*

### More Examples
``` zsh
# Use the interactive CLI decoder
python3 decode.py

# Supply a file that contains many URLs, one on each line
python3 decode.py --file="./encoded-examples.txt"

# Supply a singular URL to decode
python3 decode.py --url="https://google.com/%24"

# Supply a file, and write output to a file rather than std out
python3 decode.py --file="./urls.txt" --output="./output.txt"
```