# PDF Encryption Tool

This Python script is designed to encrypt PDF files using the AES-256 encryption algorithm. The encryption key is entered by the user during runtime, and the encrypted PDF is saved to a new file.

## Features

- Encrypts PDF files using AES-256 encryption algorithm.
- Validates the strength of the user's password.
- Ensures the existence of the input file and non-existence of the output file.
- Logs the process of encryption for debugging purposes.

## Usage

To run the script, simply execute the Python file. You will be prompted to enter a password, which will be used to encrypt the PDF file. The password must meet certain criteria to be considered strong:

- Minimum length of 8 characters.
- Must contain digits, uppercase letters, lowercase letters, and special symbols ($@#%).
- Must not contain repeating characters.
- Must not contain usernames or personal information.

## Installation

Ensure you have Python 3 and the PyPDF2 library installed on your system. You can install PyPDF2 using pip:

```bash
pip install PyPDF2
```

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or issues, feel free to reach out to the maintainer.

---
