import sys
import getpass
import hashlib
import argparse
from Crypto import Random
from Crypto.Cipher import AES


parser = argparse.ArgumentParser(
    prog = 'encrypt.py',
    usage = '\n' + 'cat {暗号化したいファイル} | python3 crypto.py -e > {ファイル名}' + '\n' +
                   'cat {暗号化されたファイル} | python3 crypto.py -d > {ファイル名}',
    description = 'Implement netcat in python',
    epilog = 'end',
    add_help = True,
)

parser.add_argument('-e', '--encrypt', help='encrypt a file', action='store_true')
parser.add_argument('-d', '--decrypt', help='decrytp a encrypted file', action='store_true')

args = parser.parse_args()

def create_aes(password, iv):
    m = hashlib.sha256()
    m.update(password.encode())
    key = m.digest()
    return AES.new(key, AES.MODE_CFB, iv)

def encrypt_func(data, password):
    iv = Random.new().read(AES.block_size)
    return iv + create_aes(password, iv).encrypt(data)

def decrypt_func(data, password):
    iv, cipher = data[:AES.block_size], data[AES.block_size:]
    return create_aes(password, iv).decrypt(cipher)

def main():
    if args.encrypt:
        
        while True:
            password = getpass.getpass('暗号化に使うパスワードを入力してください：')
            re_password = getpass.getpass('もう一度、パスワードを入力してください：')
            if password != re_password:
                continue
            else:
                break

        encrypt_file = encrypt_func(sys.stdin.buffer.read(), password)
        sys.stdout.buffer.write(encrypt_file)

    elif args.decrypt:
        password = getpass.getpass('暗号化に使用したパスワードを入力してください：')
        decrypt_file = decrypt_func(sys.stdin.buffer.read(), password)
        sys.stdout.buffer.write(decrypt_file)

    else:
        print('動作を終了します')
        sys.exit(0)

if __name__ == '__main__':
    main()
