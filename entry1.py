# AUTHOR : JAYSON CABRILLAS SAN BUENAVENTURA

import os, base64

code_of_horror = """
import os, base64

code_of_horror = '''
import os, base64

code_of_horror = "Hello, World!"

def main():
    os.system("clear")
    string_bytes = code_of_horror.encode("ascii")

    b64_encode = base64.b64encode(string_bytes)
    base64_string = b64_encode.decode("ascii")

    str_bin = " ".join(f"{ord(i):08b}" for i in base64_string)
    bin_str = "".join([chr(int(binary, 2)) for binary in str_bin.split(" ")])

    b64_decode = base64.b64decode(bin_str)
    ascii_decode = b64_decode.decode("ascii")

    print(ascii_decode)

if __name__ == "__main__":
    main()
'''

string_bytes = code_of_horror.encode("ascii")
    
def main():
    os.system("clear")
    b64_encode = base64.b64encode(string_bytes)
    base64_string = b64_encode.decode("ascii")

    str_bin = " ".join(f"{ord(i):08b}" for i in base64_string)
    
    bin_str = "".join([chr(int(binary, 2)) for binary in str_bin.split(" ")])
        
    b64_decode = base64.b64decode(bin_str)
    ascii_decode = b64_decode.decode("ascii")
    
    print(ascii_decode)

    with open('hello2.py', 'w') as f:
        f.write(ascii_decode)
    os.system("python3 hello2.py")


if __name__=="__main__":
    main()
"""

string_bytes = code_of_horror.encode("ascii")
    
def main():
    os.system("clear")
    b64_encode = base64.b64encode(string_bytes)
    base64_string = b64_encode.decode("ascii")

    str_bin = " ".join(f"{ord(i):08b}" for i in base64_string)
    
    bin_str = "".join([chr(int(binary, 2)) for binary in str_bin.split(" ")])
        
    b64_decode = base64.b64decode(bin_str)
    ascii_decode = b64_decode.decode("ascii")
    
    print(ascii_decode)

    with open('hello1.py', 'w') as f:
        f.write(ascii_decode)
    os.system("python3 hello1.py")

if __name__=="__main__":
    main()
