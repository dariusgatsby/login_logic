class User:
    def __init__(self, name) -> None:
        self.name = name
        self.is_logged_in = False
        self.password = ""

    def set_password(self):
        if self.password == "":
            new_pw = input("Enter new password: ")
            self.password = new_pw
            print(f"New password is {new_pw}")
            
        return self.password


    def login(self):
        attempts = 3
        while attempts > 0:
            if self.password != "":
                pw_attempt = input("Enter password: ")
                if pw_attempt == self.password:
                    self.is_logged_in = True
                    return "You're logged in"
                elif pw_attempt != self.password:
                    print("Wrong Password")
                    attempts -= 1
                    continue
            else:
                print("You must set a password")
                self.set_password()
        else:
            self.is_logged_in = False
            return "Too many attempts"

    def show_details(self):
        show = input("Show name, password, or both?")
        if show == "name":
            print(self.name)
        if show == "password":
            print(self.password)
        if show == "both":
            print(self.name)
            print(self.password)

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("You must login")
            print(args[0].login())
    return wrapper

@is_authenticated
def create_post(user):
        if user.is_logged_in == False:
            print(user.login())
        if user.is_logged_in == True:
            print(f"User {user.name} has created a post")
        else:
            print("Must login!")
            return None
        
@is_authenticated        
def send_message(user):
    if user.is_logged_in == True:
        message = input("enter message: ")
        print(f"User {user.name} has sent a message: {message}")
    else:
        print("Must login!")
        return None

           
name = input("Name for Account: ")
user = User(name)
accessing = True
while accessing == True:
    ask = input("Create a post, send message, settings or exit? ")
    if ask == "post":
        create_post(user)
        made_post = True
    elif ask == "message":
        send_message(user)
    elif ask == "exit":
        print("Bye!")
        accessing = False
        break
    elif ask == "logout":
        user.is_logged_in = False
        print("You logged out")
        continue
    elif ask == "settings":
        user.show_details()
    else:
        print("Enter valid option")
        continue