import secrets

def generate_cipher_key():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    symbols = '!@#$%^&*_+-<?>,:./~'
    all_characters = list(alphabet + ' ' + symbols)
    
    shuffled_characters = list(all_characters)
    secrets.SystemRandom().shuffle(shuffled_characters)
    
    cipher_key = dict(zip(all_characters, shuffled_characters))
    
    return cipher_key

def save_key_to_file(key, filename='cipher_key.txt'):
    with open(filename, 'w') as file:
        for k, v in key.items():
            file.write(f"{k}={v}\n")

def load_key_from_file(filename='cipher_key.txt'):
    key = {}
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if content:
                for line_number, line in enumerate(content.split('\n'), start=1):
                    parts = line.strip().split('=')
                    if len(parts) == 2:
                        k, v = parts
                        key[k] = v
                    else:
                        raise ValueError(f"Invalid key format in line {line_number} of the file.")
    except FileNotFoundError:
        print(f"Error: Key file '{filename}' not found. Generating a new key.")
        return generate_cipher_key()  # Generate a new key if file is missing
    except Exception as e:
        print(f"Error loading key: {e}")
        return None  # Return None in case of other errors

    return key



def encryption(txt, key):
    encrypted_chars = [key.get(char, char) for char in txt]
    encrypted = ''.join(encrypted_chars)
    return encrypted

def decryption(encrypted_data, key):
    reversed_key = {v: k for k, v in key.items()}
    decrypted_chars = [reversed_key.get(char, char) for char in encrypted_data]
    decrypted = ''.join(decrypted_chars)
    return decrypted

def main():
    d = input("Enter your secret message: ")
    
    key = generate_cipher_key()
    
    encrypted_message = encryption(d, key)
    print("Encrypted message:", encrypted_message)
    
    save_key_to_file(key)  # Save the key for later decryption
    
    loaded_key = load_key_from_file()
    if loaded_key:  # Check if a valid key was loaded
        decrypted_message = decryption(encrypted_message, loaded_key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Decryption failed due to invalid key.")


if __name__ == "__main__":
    main()
