# iss program main hum password hashing krein gay password ko encrypt kreingay hash main convert krein
# gay hamara password jesa hum daltay wesay store nhi hota pehlay woo hash bnta phir woo store hota hai
# takay password secure rahay.

from hashlib import sha256


# Ye function check karta hai ke user ka diya huay password ka hash, stored hash ke barabar hai ya nahi.
def login(email, stored_logins, password_to_check):
    
    # dictionary kee key say value dictionary kee jokay password hai hashed form main store woo access krkay store krdiya variable main
    stored_password = stored_logins[email]

    # user kay diye huay password ka hash_password function say jo hashed pass bana woo input_password main store krdiya
    input_password = hash_password(password_to_check)


    # Comparison agar stored hash user kay hash say milta hai tw true warna false
    if stored_password == input_password:
        return True
    else:
        return False



# Ye function password ko hash (encrypted code) mein convert karta hai.
def hash_password(password):

    encode_pass = password.encode() # Password ko "encode" kiya (text → bytes)
    hashed_password = sha256(encode_pass).hexdigest() # SHA256 hash generate kiya
    return hashed_password # hash return krdiya

    # esay bhee likhsktay 1 line main
    # return sha256(password.encode()).hexdigest()



def main():

    # dictionary
    stored_logins: dict = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }


    # Test Cases mtlb test case batata kay program sahi hai yani kay result jo ana chahiye wohi aya jo input diya uskay
    # according jesay abhi true aya tw access doo false aya tw deny yeh test case hai.
    print(login('example@gmail.com', stored_logins, 'word'))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))



if __name__ == '__main__':
    main()