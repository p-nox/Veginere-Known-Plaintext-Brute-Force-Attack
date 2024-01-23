import time
from itertools import  product
import sys

def decrypt(cipherText, key):
        #convert cipherText and key to Ascii
        cipher_Ascii = [ord(letter) for letter in cipherText]
        key_Ascii = [ord(letter) for letter in key]
        plain_Ascii = []
        #decrypt cipherText by permuting the symbols with the value of the key in the Ascii table
        for i in range(len(cipher_Ascii)):
            plain_Ascii.append(((cipher_Ascii[i]-key_Ascii[i % len(key)]) % 26) + 97)
        plaintext = ''.join(chr(i) for i in plain_Ascii)
        return plaintext
    
def crack(cipherText, knownPlainText, keyLength):
        alphaBet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        start_time = time.time()
        attempts = 0
        print ("Cracking:",cipherText)
        #this is my key generator sequence
        #product function produce combinations of alphabet letters in this format('A','A','A','A','A','A',)
        #and with .join i transpose them to this format('AAAAAA')
        for key in map(''.join, product(alphaBet, repeat=keyLength)):
                attempts +=1
                #cypherText decryption with the generated key
                PlainText = decrypt(cipherText, key)
                #condition to find the cypher key
                if PlainText.upper() == knownPlainText.upper() : break
                  
        print("++++++++++++++++++++++++++++++++++++++++++")            
        print("-> Total time: %s seconds " % (time.time() - start_time))
        print("-> Attempts: ", attempts, "Key: ", key)
        print("++++++++++++++++++++++++++++++++++++++++++")
        return PlainText
    
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        sys.exit(1)
        
if __name__ == "__main__":
    
    if len(sys.argv) != 4:
            print("Usage: <source> <path for cypher> <path for plain> <key lenght>", file=sys.stderr)
            sys.exit(-1)
        
    cipherText = read_file(sys.argv[1])
    plainText = read_file(sys.argv[2])
    keyLength = int(sys.argv[3])
   
    crack(cipherText, plainText, keyLength)  
    

#crack('VIEOEGMOCIGOHHJGBALOTMRJBHUMPXRJKQAMMBZAZKLMROROMQRAAUMNFWUGKXRNGKKUCTXKXJLXGNXAFWQCHLBIAJLJVVQSHLVBVSXQZBUIKSGBBUEUELFZNXPKNXXZLTYEMBVIIGBFRJYKUIFSFGGXUWAUMZFZTKMNYIGNXVZOTKLNSWBQBMZVGNXCEBRXGYK','CONGRATULATIONSYOUSUCEEDINDECRYPTINGTHISMESSAGEITWASNOTTOOHARDAFTERALLKEEPUPTHEGOODWORKANDSPENDMORETIMEWITHCRYPTOOLANDSTUDYCAREFULLYTHEAVAILABLEBOOKSANDDONOTFORGETTHATHEBIGGESTBOOKISINTHEINTERNET',6)
    