import os
import logging
import re
from pypdf import PdfReader, PdfWriter
from getpass import getpass

# Define constants
INPUT_FILE = 'data.pdf'
OUTPUT_FILE = 'protected.pdf'
PASSWORD_PROMPT = 'Enter password: '
ENCRYPTION_ALGORITHM = "AES-256"

def ensure_file_exists(filename):
 filename = os.path.abspath(filename)
 if not os.path.exists(filename):
    raise FileNotFoundError(f"File {filename} does not exist.")
 return filename

def validate_password(password):
 # Check minimum length of password
 if len(password) < 8:
    return False

 # Check presence of characters from three categories
 has_digit = any(char.isdigit() for char in password)
 has_upper = any(char.isupper() for char in password)
 has_lower = any(char.islower() for char in password)
 
 if not has_digit or not has_upper or not has_lower:
    return False

 # Check presence of special symbols
 special_symbols = ['$', '@', '#', '%']
 has_special = any(char in special_symbols for char in password)
 
 if not has_special:
    return False

 # Check for repeating characters
 repeated_chars = r'(.)\1+'
 if re.search(repeated_chars, password):
    return False

 # Check for usage of username or personal information
 # Here we assume that usernames are stored in a list 'usernames'
 usernames = ['username1', 'username2', 'username3']
 if any(username in password for username in usernames):
    return False

 return True

def encrypt_pdf(input_file, output_file):
 input_file = ensure_file_exists(input_file)

 output_file = os.path.abspath(output_file)
 if os.path.exists(output_file):
    raise FileExistsError(f"File {output_file} already exists.")

 reader = PdfReader(input_file)
 writer = PdfWriter()

 for page in reader.pages:
    writer.add_page(page)

 password = getpass(prompt=PASSWORD_PROMPT)
 if not validate_password(password):
    raise ValueError(f"Invalid password.")

 try:
    with open(output_file, 'wb') as file:
        writer.encrypt(password, algorithm=ENCRYPTION_ALGORITHM)
        writer.write(file)
        logging.info("Successfully wrote to the file %s.", output_file)
 except IOError as e:
    logging.error("An error occurred while writing to the file %s: %s", output_file, str(e))
 except Exception as e:
    logging.error("An unexpected error occurred: %s", str(e))

if __name__ == "__main__":
 encrypt_pdf(INPUT_FILE, OUTPUT_FILE)
