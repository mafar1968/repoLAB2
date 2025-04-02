from cryptography.fernet import Fernet

# Gera uma nova chave Fernet
key = Fernet.generate_key()

# Nome do arquivo onde a chave será gravada
file_name = 'key.fernet'

# Grava a chave no arquivo
with open(file_name, 'wb') as key_file:
    key_file.write(key)

print(f'Chave gerada e gravada em {file_name}')