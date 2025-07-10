# Simple Substitution Cipher Cracker

## Overview
This Python script provides a basic implementation of a cipher cracker using a brute-force approach to find the key for a given cipher text. It supports decryption of a cipher text by trying all possible combinations of a specified key length and comparing the result with a known plain text.

---

## Features
- Brute-force approach to crack simple substitution cipher
- Supports variable key length
- Provides information on the total time taken and the number of attempts made during the key-cracking process.
- Works with input files (ciphertext and plaintext)

---

## Usage

To execute: ```python script_name.py <path_for_cipher> <path_for_plain> <key_length>```

 * **path_for_cipher:** The cipher text to be decrypted.
 * **path_for_plain:** The known plain text used to verify the correctness of the decryption.
 * **key_length:** The length of the key to be used in the brute-force attack

---

## Algorithm

  * Uses itertools.product to generate all combinations of uppercase letters of the specified length.
  * Tries each key and decrypts the ciphertext using a Vigenère decryption formula.
  * Compares the resulting plaintext with the known text to find a match.
  * Stops at the first correct match and prints time and attempt count.

---

## Note

This script is designed for educational purposes and may not be suitable for large key spaces or complex encryption algorithms. It uses a basic brute-force approach and may not be efficient for cryptographic purposes.
Ensure that the provided plaintext is indeed present in the encrypted text, as the script relies on a known plaintext attack.

Feel free to explore and modify the script based on your requirements.
