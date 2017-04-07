import time
import subprocess
import hashlib

class GetHashValue: 
    
    def __init__(self, get_hash, hashed_value):
        self.get_hash = get_hash
        self.hashed_value = hashed_value

    @classmethod
    def hash_value(cls):
        print('''
        Python3 Multiple Condensed Basic Alogrithmic Hasher
                    P.M.C.B.A.H v1.2.0
                  Author: scriptedp0ison
        ---------------------------------------------------
        ''')
        try:
            cls.get_hash = input('[+] Enter a value to hash: ')
            time.sleep(1)
            log_input = cls.get_hash
            print('[+] Data from user input stored successfully!')
            time.sleep(2)
        except NameError:
            print('[+] You forgot to put ""\'s around your input! Switching to raw_input function instead...')
            time.sleep(3)
            GetHashValue.get_hash_raw()
        else:
            GetHashValue.hashed_value()

    @classmethod
    def get_hash_raw(cls):
        cls.get_hash = raw_input('[+] Enter a value to hash: ')
        time.sleep(1)
        log_input = cls.get_hash
        print('[+] Data from user input stored successfully!')
        time.sleep(2)
        GetHashValue.hashed_value
            
            
    @classmethod
    def hashed_value(cls):
        hash = raw_input('[+] Your input is ready to be hashed! Choose an algorithm to hash data?: ')
        if((hash == 'yes') or (hash == 'y')):
            print('''
            1.) MD5 (UNSECURE)
            2.) MD4 (UNSECURE)
            3.) SHA1
            4.) SHA384
            5.) SHA224
            6.) SHA512
            7.) SHA256
            8.) BLAKE2B512 (DEPRICATED)
            9.) BLAKE2S56 (DEPRICATED)
            10.) RIPEMD160 (DEPRICATED)
            -------------------------------------------------------------------
            ''')
            cls.hashed_value = int(input('[+] Choose an encryption to use below: ')) 
            #set the hash to MD5
            if(cls.hashed_value == 1):
                print('[+] Hash Algorithm set to: MD5')
                time.sleep(3)
                try:
                    convert_hash = hashlib.md5(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
            
            #set the hash to MD4
            elif(cls.hashed_value == 2):
                print('[+] Hash Algorithm set to: MD4')
                time.sleep(3)
                try:
                    convert_hash = hashlib.md4(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
            
            #set the hash to SHA1
            elif(cls.hashed_value == 3):
                print('[+] Hash Algorithm set to: SHA1')
                time.sleep(3)
                try:
                    convert_hash = hashlib.sha1(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
            
            #set the hash to SHA384
            elif(cls.hashed_value == 4):
                print('[+] Hash Algorithm set to: SHA384')
                time.sleep(3)
                try:
                    convert_hash = hashlib.sha384(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
            
            #set hash to SHA224
            elif(cls.hashed_value == 5):
                print('[+] Hash Algorithm set to: SHA224')
                time.sleep(3)
                try:
                    convert_hash = hashlib.sha224(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
                
            #set hash to SHA512
            elif(cls.hashed_value == 6):
                print('[+] Hash Algorithm set to: SHA512')
                time.sleep(3)
                try:
                    convert_hash = hashlib.sha512(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()

            #set hash to SHA256
            elif(cls.hashed_value == 7):
                print('[+] Hash Algorithm set to: SHA256')
                time.sleep(3)
                try:
                    convert_hash = hashlib.sha256(b'{}'.format(cls.get_hash))
                    convert_hexdigest = convert_hash.hexdigest()
                except Exception:
                    print('[+] The Hashed output was lost! Exitting...')
                    exit()
                else:
                    print('[+] User input was successfully hashed! Printing output...')
                    time.sleep(2)
                    print('Your hashed value for {} is: {}'.format(cls.get_hash, convert_hexdigest))
                    call_stack = raw_input('[+] Hash another value via Algorithmic encryption: ')
                    if call_stack == 'yes' or call_stack == 'y':
                        subprocess.call('clear', shell=True)
                        GetHashValue.hash_value()
                    elif call_stack == 'no' or 'n':
                        print('[+] Got user defined exit! Exitting...')
                        time.sleep(3)
                        exit()
            
            #if user enters the hash value of 8 throw error
            elif(cls.hashed_value == 8):
                get_error = raw_input('[+] Error! The option {} is invalid! The hash algorithm BLAKE2B512 is missing! Return to algorithm set:  '.format(cls.hashed_value))
                if(get_error == 'yes') or (get_error == 'y'):
                    print('[+] Returning to algorithm...')
                    time.sleep(2)
                    GetHashValue.hashed_value()
                elif(get_error == 'no') or (get_error == 'n'):
                    exit_encr = ('[+] Algorithm hash aborted! Exit: ')
                    if exit_encr == 'yes' or 'y':
                        print('[+] Exitting...')
                        time.sleep(3)
                        exit()
                    elif exit_encr == 'no' or 'n':
                        print('[+] Returning to hash function...(*Press Ctrl+C to quit*)')
                        time.sleep(3)
                        GetHashValue.hashed_value()
                    else:
                        print('[+] Value was not defined! Exitting...')
                        time.sleep(3)
                        exit()

            #if user enters in the hash value of 9 throw error 
            elif(cls.hashed_value == 9):
                get_error = raw_input('[+] Error! The option {} is invalid! The hash algorithm BLAKE2S56 is missing! Return to algorithm set:  '.format(cls.hashed_value))
                if(get_error == 'yes') or (get_error == 'y'):
                    print('[+] Returning to algorithm...')
                    time.sleep(2)
                    GetHashValue.hashed_value()
                elif(get_error == 'no') or (get_error == 'n'):
                    exit_encr = ('[+] Algorithm hash aborted! Exit: ')
                    if exit_encr == 'yes' or 'y':
                        print('[+] Exitting...')
                        time.sleep(3)
                        exit()
                    elif exit_encr == 'no' or 'n':
                        print('[+] Returning to hash function...(*Press Ctrl+C to quit*)')
                        time.sleep(3)
                        GetHashValue.hashed_value()
                    else:
                        print('[+] Value was not defined! Exitting...')
                        time.sleep(3)
                        exit()
                        
            
            #if user enters in the hash value of 10, throw error
            elif(cls.hashed_value == 10):
                get_error = raw_input('[+] Error! The option {} is invalid! The hash algorithm RIPEMD160 is missing! Return to algorithm set:  '.format(cls.hashed_value))
                if(get_error == 'yes') or (get_error == 'y'):
                    print('[+] Returning to algorithm...')
                    time.sleep(2)
                    GetHashValue.hashed_value()
                elif(get_error == 'no') or (get_error == 'n'):
                    exit_encr = ('[+] Algorithm hash aborted! Exit: ')
                    if exit_encr == 'yes' or 'y':
                        print('[+] Exitting...')
                        time.sleep(3)
                        exit()
                    elif exit_encr == 'no' or 'n':
                        print('[+] Returning to hash function...(*Press Ctrl+C to quit*)')
                        time.sleep(3)
                        GetHashValue.hashed_value()
                    else:
                        print('[+] Value was not defined! Exitting...')
                        time.sleep(3)
                        exit()
    
#run script if running python file directly
if __name__ == '__main__':
    GetHashValue.hash_value()
