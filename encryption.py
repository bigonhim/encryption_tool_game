from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a cipher object with the key
cipher = Fernet(key)

# Data to be encrypted
data_to_encrypt = b"Hello, sensitive information!"

# Encrypt the data
encrypted_data = cipher.encrypt(data_to_encrypt)

decrypted_data=cipher.decrypt(encrypted_data)

print(encrypted_data)
print("HELLO HUMAN TO GET BACK YOUR FILES PAY US 3000$!!!")
Answer=input("Will you comply  YES/NO : ").lower()

Answers=['yes','y','yeah']
if Answer in Answers:
       print("Pay to this number: 0716010405 ")
       while True:
              Payment=float(input("input the money: " ))
              if Payment >= 3000 :
                     print("HERE IS THE CODE")
                     print(decrypted_data)
                     
                     break
              else :
               print("NOT ENOUGH PLEASE")  
               continue          
else :
       print("Goodluck getting the data!")



   







