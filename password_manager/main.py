from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key) 
        
# write_key()    

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_password = input("\nSet your master password: ")

key = load_key()
fer = Fernet(key)


    
def view():
    with open("passwords.txt", "r") as f:
        for line in f:
            try:
                print(fer.decrypt(line.strip().encode()).decode())
            except:
                print(line.strip()) 

         

def add():
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(f"\nUsername: {name}\n")
        f.write(f"Password: {fer.encrypt(password.encode()).decode()}\n")
        f.write("___________________________")

while(True):
    print("Would you like to add a new password or view the existing passwords? (Press q to quit)")
    mode = input("Choose view or add: ").lower()

    if mode == "q":
        break
        
    elif mode == "view":
        view()
        
    elif mode == "add":
        add()
        
    else:
        print("Invalid mode!")
        continue
    