from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def encrypt_bmp(input_file, output_file, key, mode):
    HEADER_SIZE = 54  # Tamanho do cabeçalho BMP padrão

    # Ler a imagem BMP
    with open(input_file, 'rb') as f:
        header = f.read(HEADER_SIZE)  # Ler o cabeçalho
        body = f.read()  # Ler o corpo da imagem

    # Criar cifra AES
    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        iv = None
    elif mode == "CBC":
        iv = os.urandom(16)  # Gerar um IV aleatório para CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Modo inválido. Use 'ECB' ou 'CBC'.")

    # Aplicar padding e cifrar
    encrypted_body = cipher.encrypt(pad(body, AES.block_size))

    # Criar o arquivo de saída
    with open(output_file, 'wb') as f:
        f.write(header)  # Manter o cabeçalho original
        if mode == "CBC":
            f.write(iv)  # Armazenar o IV no início do corpo cifrado
        f.write(encrypted_body)  # Escrever o corpo cifrado

# Definir chave AES de 16 bytes (AES-128)
key = os.urandom(16)  # Chave aleatória

# Cifrar a imagem com AES-ECB
encrypt_bmp('c-academy.bmp', 'c-academy-encrypted-ECB.bmp', key, 'ECB')

# Cifrar a imagem com AES-CBC
encrypt_bmp('c-academy.bmp', 'c-academy-encrypted-CBC.bmp', key, 'CBC')

print("Imagens cifradas com AES-ECB e AES-CBC.")
