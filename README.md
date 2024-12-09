# coded-repository
This project provides tools to encode and decode text using a secure key. The encoded data is stored in `.md` files within a `database/` directory, ensuring privacy and structured management. The project uses a fixed, secure key for encoding and decoding, preventing unauthorized use.

---

## Features
- **Text Encoding**: Encode a string and save it in a randomly named `.md` file.
- **Text Decoding**: Decode the contents of an encoded `.md` file back to its original text.
- **Secure Key Verification**: Ensures that only the correct, fixed key can be used.
- **Environment Variable Management**: Supports `.env` files to store sensitive configurations.

---

## Project Structure
```
.
├── database/        # Directory where encoded files are stored
├── .env             # Stores the ENCODING_KEY (ignored by Git)
├── .gitignore       # Ensures sensitive files are excluded from version control
├── encode.py        # Script to encode text and save to file
├── decode.py        # Script to decode text from an encoded file
├── README.md        # Project documentation
```

---

## Requirements
- Python 3.6+
- The following Python packages:
  - `python-dotenv`

---

## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install python-dotenv
   ```

3. **Create the `.env` File**:
   Create a `.env` file in the project root with the following content:
   ```plaintext
   ENCODING_KEY=contact +923074518566 to get the key
   ```

4. **Ensure `.gitignore**:
   The `.gitignore` file already excludes the `.env` file and the `database/` directory from version control:
   ```plaintext
   # Ignore environment files
   .env

   # Ignore database directory
   database/
   ```

---

## Usage

### Encoding Text
1. Open the `encode.py` file and run the script:
   ```bash
   python encode.py
   ```
2. The script will encode a predefined string and save it as a `.md` file in the `database/` directory.
3. Output Example:
   ```
   File created: database/abc123xyz4567890.md
   ```

### Decoding Text
1. Run the `decode.py` file:
   ```bash
   python decode.py
   ```
2. Provide the name of the `.md` file you want to decode (e.g., `abc123xyz4567890.md`).
3. If the correct key is used, the original text is displayed.

---

## Security Measures
1. **Fixed Key**: The encoding key is securely hashed and verified to prevent misuse. Only the original, hardcoded key is allowed.
2. **Key Verification**: The script hashes the key from the `.env` file and matches it against the pre-stored hash. If they don’t match, the program exits.
3. **.gitignore**: Sensitive files, such as `.env` and the `database/` directory, are excluded from version control.

---

## Limitations
- The key is fixed and must be manually updated in the script if it ever needs to change.
- This project is intended for educational purposes and should not be used for highly sensitive data.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.