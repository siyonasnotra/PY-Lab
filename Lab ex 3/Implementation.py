import pyqrcode
import png
import UserModule

users = [{"name": "siyona", "gender": "F", "username": "siyonasnotra", "password": "siyona@snotra",
          "email": "siyona.snotra@gmail.com", "phone": 9717361508}]

while True:
    menu = '''
    1. To create new user (not add them to database): Press 1
    2. To add a user using SmartScan : Press 2
    3. To fetch all users : Press 3
    4. To add users manually (without qr) : Press 4
    5. To exit code : Press 5
    '''
    print(menu)
    option = int(input("enter your choice : "))
    print("* " * 20)

    if option == 1:
        data_dict = UserModule.get_user_input()
        check = UserModule.validation(data_dict)

        if check != 0:
            if check == 1:
                print("Invalid name")
            if check == 2:
                print("Invalid gender")
            if check == 3:
                print("Invalid phone")
            if check == 4:
                print("Invalid username")
            if check == 5:
                print("Invalid email")
            continue

        UserModule.encode_dict_to_qr(data_dict, data_dict["username"] + ".png")
        print("QR for user", data_dict["username"], "is generated")

    elif option == 2:
        try:
            username = input("enter the username of the user : ")
            UserModule.smartScan(username + ".png", users)
        except:
            print("QR code is not present")

    elif option == 3:
        UserModule.show_users(users)

    elif option == 4:
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        data_dict = UserModule.create_user_dict_lambda(name, gender, username, password, email, phone)
        check = UserModule.validation(data_dict)

        if check != 0:
            if check == 1:
                print("Invalid name")
            if check == 2:
                print("Invalid gender")
            if check == 3:
                print("Invalid phone")
            if check == 4:
                print("Invalid username")
            if check == 5:
                print("Invalid email")
            continue

        users = UserModule.add_user_to_list_lambda(data_dict, users)

    elif option == 5:
        break
