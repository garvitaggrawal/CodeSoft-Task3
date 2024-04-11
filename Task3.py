import string
import secrets
len=int(input("Enter the lenght of password:"))
mix_chr=string.digits+string.ascii_letters+string.punctuation
password=''
for i in range(len):
    password+=''.join(secrets.choice(mix_chr))
print(password)