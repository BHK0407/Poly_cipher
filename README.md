# Poly-Alphabetic Substitution Cipher

This Python script implements a poly-alphabetic substitution cipher to encrypt and decrypt messages. The script uses a key to generate a character mapping for substitution, providing a basic form of encryption.

# Functionality

- The **'poly'** function takes a plaintext and a key as input and performs poly-alphabetic substitution encryption or decryption.

- The script supports both encryption and decryption through the generated character mapping.

- Non-alphabetic characters in the input text are preserved during the process.

# License

This project is licensed under the MIT License.

# Usage

**Clone the Repository:**
   ```bash
   git clone https://github.com/BHK0407/BHK0407-Poly_cipher.git

1. Navigate to the Project Directory:

bash

cd poly_cipher

2. Run the Script:

bash

python poly_cipher.py

3. Input Cipher Text and View Results:
Modify the poly function call with your cipher text and iterate through possible keys in the specified range.

python
for i in range(26):
    # For example my cipher text input is XTKG XTKMA LNKOXR LEBF
    possible_answer = poly("XTKG XTKMA LNKOXR LEBF", i)
    print(f"{possible_answer.upper()}, Key: {i + 1}")

