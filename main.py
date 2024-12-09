import os
import random
import string
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve the encoding key from the .env file
encoding_key = int(os.getenv("ENCODING_KEY", 0))  # Default to 0 if not found

# Function to encode the text using the key
def encode_text(text, key):
    encoded_chars = []
    key_str = str(key)
    key_length = len(key_str)
    for i, char in enumerate(text):
        key_digit = int(key_str[i % key_length])  # Rotate through the digits of the key
        encoded_char = chr((ord(char) + key_digit) % 256)
        encoded_chars.append(encoded_char)
    return ''.join(encoded_chars)

# Function to generate a random 16-character filename
def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

# Function to ensure the .gitignore file exists
def create_gitignore():
    gitignore_content = """
# Ignore .env files
.env

# Ignore database directory
database/
"""
    with open(".gitignore", "w") as gitignore_file:
        gitignore_file.write(gitignore_content.strip())
    print(".gitignore created/updated.")

# Main function to create the encoded file
def create_encoded_file(text):
    if encoding_key == 0:
        print("Error: Encoding key is not set in the .env file.")
        return
    
    encoded_text = encode_text(text, encoding_key)
    random_filename = generate_random_filename() + ".md"
    
    # Ensure the database directory exists
    os.makedirs("database", exist_ok=True)
    
    # Save the encoded text to a file in the database directory
    file_path = os.path.join("database", random_filename)
    with open(file_path, "w") as file:
        file.write(encoded_text)
    
    print(f"File created: {file_path}")

if __name__ == "__main__":
    input_text = "This is the text to be encoded!"
    create_encoded_file(input_text)
