# Dictionary of common percent encoded characters

import argparse
import re

encoded_characters = {
    "%20": " ",
    "%21": "!",
    "%22": "\"",
    "%23": "#",
    "%24": "$",
    "%25": "%",
    "%26": "&",
    "%27": "'",
    "%28": "(",
    "%29": ")",
    "%2A": "*",
    "%2B": "+",
    "%2C": ",",
    "%2D": "-",
    str("%2E"): ".",
    str("%2F"): "/",
    "%30": "0",
    "%31": "1",
    "%32": "2",
    "%33": "3",
    "%34": "4",
    "%35": "5",
    "%36": "6",
    "%37": "7",
    "%38": "8",
    "%39": "9",
    "%3A": ":",
    "%3B": ";",
    "%3C": "<",
    "%3D": "=",
    str("%3E"): ">",
    str("%3F"): "?",
    "%40": "@",
    "%41": "A",
    "%42": "B",
    "%43": "C",
    "%44": "D",
    "%45": "E",
    "%46": "F",
    "%47": "G",
    "%48": "H",
    "%49": "I",
    "%4A": "J",
    "%4B": "K",
    "%4C": "L",
    "%4D": "M",
    "%4E": "N",
    "%4F": "O",
    "%50": "P",
    "%51": "Q",
    "%52": "R",
    "%53": "S",
    "%54": "T",
    "%55": "U",
    "%56": "V",
    "%57": "W",
    "%58": "X",
    "%59": "Y",
    "%5A": "Z",
    "%5B": "[",
    "%5C": "\\",
    "%5D": "]",
    "%5E": "^",
    "%5F": "_",
    "%60": "`",
    "%61": "a",
    "%62": "b",
    "%63": "c",
    "%64": "d",
    "%65": "e",
    "%66": "f",
    "%67": "g",
    "%68": "h",
    "%69": "i",
    "%6A": "j",
    "%6B": "k",
    "%6C": "l",
    "%6D": "m",
    str("%6E"): "n",
    str("%6F"): "o",
    "%70": "p",
    "%71": "q",
    "%72": "r",
    "%73": "s",
    "%74": "t",
    "%75": "u",
    "%76": "v",
    "%77": "w",
    "%78": "x",
    "%79": "y",
    "%7A": "z",
    "%7B": "{",
    "%7C": "|",
    "%7D": "}",
    str("%7E"): "~",
    str("%7F"): " "
}

# Decode a supplied URL
def DecodeString(URL):

    # Split the URL and return a list, broken up by the encoded chars
    Pattern = r'(%..)'
    Parts = re.split(Pattern, URL)
    Broken_Up_URL = [part for part in Parts if part]
    
    # Create an empty list to put the new decoded URL bits in
    Decoded_URL = []

    for i in Broken_Up_URL:
        if i in encoded_characters.keys():
            Decoded_URL += encoded_characters[i]
        else:
            Decoded_URL += i

    return ''.join(Decoded_URL)

def main():
    # Create parser object for arguments passed when running the script
    parser = argparse.ArgumentParser()

    # --file is for specifying a file with a bunch of URLs. --url is for
    # specifying an individual URL to decode
    parser.add_argument('--url', help='Specify a URL to decode')
    parser.add_argument('--file', help='Specify a file with many URLs to decode (one per line)')
    parser.add_argument('--output', help='Specify a file name to send output to')
    args = parser.parse_args()

    # Depending on the arguments supplied, decode the given url(s) and send to specified (or unspecified) output
    if args.url:
        if args.output:
            # if --output is supplied, write to the specified file, unless there is an issue with what was supplied
            try:
                with open(args.output, 'a') as file:
                    file.write(DecodeString(args.url))
            except:
                print("Error writing to file. Use a real path.")
        else:
            # If no output file supplied, just write to std output
            print(DecodeString(args.url))
    elif args.file:
        try:
            # Open the file, read each line
            with open(args.file, 'r') as file:
                for line in file:
                    line = line.strip()

                    # If output supplied, write to it otherwise use std out
                    if args.output:
                        with open(args.output, 'a') as file:
                            file.write(DecodeString(line))
                            file.write("\n")
                            print(DecodeString(line))
                    else:
                        print(DecodeString(line))
        except:
            print("File not found:", args.file)
    else:
        # If no args supplied, run an interactive decoder
        URL = input("\nEnter encoded URL: ")
        print("\nDecoded URL:", DecodeString(URL), "\n")

if __name__ == "__main__":
    main()