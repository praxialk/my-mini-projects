import secrets
import string
import sys

def generate_password(length=16, include_numbers=True, include_symbols=True):
    # Base character set
    characters = string.ascii_letters 
    
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
        
    # Generate secure random choice for each character
    return ''.join(secrets.choice(characters) for i in range(length))

if __name__ == "__main__":
    pwd_length = 16
    if len(sys.argv) > 1:
        try:
            pwd_length = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer for password length.")
            sys.exit(1)
            
    # The secrets module provides cryptographic security, avoiding the predictable pseudorandomness of `random`.
    secure_password = generate_password(length=pwd_length)
    
    print("\n--- Secure Password Generator ---\n")
    print(f"Password ({pwd_length} chars):  {secure_password}")
    print("\nWarning: Make sure to store this securely!\n")
