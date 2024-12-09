import os
import hashlib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Expected hashed key (computed beforehand using your fixed key)
EXPECTED_HASH = "4be17dfbxc92b39bc927986f6a42c4f68b0f93488f1b5271518c19f7a6ee4d95"

def verify_key(key):
    # Compute the hash of the provided key
    key_hash = hashlib.sha256(str(key).encode()).hexdigest()
    return key_hash == EXPECTED_HASH

# Function to decode the text
def decode_text(encoded_text, key):
    decoded_chars = []
    key_str = str(key)
    key_length = len(key_str)
    for i, char in enumerate(encoded_text):
        key_digit = int(key_str[i % key_length])  # Rotate through the digits of the key
        decoded_char = chr((ord(char) - key_digit) % 256)
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)

# Function to read and decode the file
def decode_file(file_name):
    key = os.getenv("ENCODING_KEY")
    if not key:
        print("Error: ENCODING_KEY not found in the .env file.")
        return

    if not verify_key(key):
        print("Error: The provided ENCODING_KEY is invalid.")
        return
    
    file_path = os.path.join("database", file_name)
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' does not exist in the 'database/' directory.")
        return
    
    # Read the encoded text from the file
    with open(file_path, "r") as file:
        encoded_text = file.read()
    
    # Decode the text
    decoded_text = decode_text(encoded_text, key)
    print("Decoded Text:")
    print(decoded_text)

if __name__ == "__main__":
    # Example usage
    file_name = input("Enter the name of the .md file to decode: ")
    decode_file(file_name)
