import time
from itertools import  product

def decrypt( cipherText, key):
        #convert cipherText and key to Ascii
        cipher_Ascii = [ord(letter) for letter in cipherText]
        key_Ascii = [ord(letter) for letter in key]
        plain_Ascii = []
        #decrypt cipherText by permuting the symbols with the value of the key in the Ascii table
        for i in range(len(cipher_Ascii)):
            plain_Ascii.append(((cipher_Ascii[i]-key_Ascii[i % len(key)]) % 26) + 97)
        plaintext = ''.join(chr(i) for i in plain_Ascii)
        return plaintext
    
def crack( cipherText, knownPlainText, keyLength):
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
    
crack('VIEOEGMOCIGOHHJGBALOTMRJBHUMPXRJKQAMMBZAZKLMROROMQRAAUMNFWUGKXRNGKKUCTXKXJLXGNXAFWQCHLBIAJLJVVQSHLVBVSXQZBUIKSGBBUEUELFZNXPKNXXZLTYEMBVIIGBFRJYKUIFSFGGXUWAUMZFZTKMNYIGNXVZOTKLNSWBQBMZVGNXCEBRXGYK','CONGRATULATIONSYOUSUCEEDINDECRYPTINGTHISMESSAGEITWASNOTTOOHARDAFTERALLKEEPUPTHEGOODWORKANDSPENDMORETIMEWITHCRYPTOOLANDSTUDYCAREFULLYTHEAVAILABLEBOOKSANDDONOTFORGETTHATHEBIGGESTBOOKISINTHEINTERNET',6)

def read_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            
            # Ensure that there are exactly two lines in the file
            if len(lines) != 2:
                raise ValueError("File must contain exactly two lines: one for ciphertext and one for known plaintext.")
            
            # Return the ciphertext and known plaintext as a tuple
            return lines[0].strip(), lines[1].strip()
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")