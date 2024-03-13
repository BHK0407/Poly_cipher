import string


# Function to perform the poly-alphabetic substitution cipher
def poly(plain: str, key: int) -> str:
    # Convert the plaintext to lowercase for consistency
    plain = plain.lower()
    # Initialize an empty dictionary to store character mappings
    charset = {}

    # Generate the alphabet
    letters = string.ascii_lowercase

    # Create a dictionary for character substitution based on the key
    for i in range(len(letters)):
        charset[letters[i - key]] = letters[i]

    # Function to perform encryption/decryption using the generated charset

    def encdec(plain: str, charset: dict) -> str:
        encrypted_string = ''

        for char in plain:
            if char.isalpha():
                # Handle uppercase letters and substitute based on charset
                if char.isupper():
                    encrypted_string += charset[char.lower()].upper()
                else:
                    encrypted_string += charset[char]
            else:
                # Preserve non-alphabetic characters
                encrypted_string += char

        return encrypted_string
    # Return the result of encryption/decryption
    return encdec(plain, charset)

# Iterate through all possible keys in the range [0, 25]
for i in range(26):
    # Input the cipher text
    # For example my cipher text is XTKG XTKMA LNKOXR LEBF
    possible_answer = poly("XTKG XTKMA LNKOXR LEBF", i)
    print(f"{possible_answer.upper()}, Key: {i + 1}")
