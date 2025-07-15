# cli.py
import argparse
from caesar_cipher.core import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose operation")
    parser.add_argument("message", help="Message to process")
    parser.add_argument("shift", type=int, help="Shift value")
    args = parser.parse_args()

    if args.mode == "encrypt":
        print("Encrypted:", encrypt(args.message, args.shift))
    else:
        print("Decrypted:", decrypt(args.message, args.shift))

if __name__ == "__main__":
    main()

