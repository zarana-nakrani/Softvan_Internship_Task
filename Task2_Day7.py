class Error(Exception):
    pass


class LengthException(Error):
    pass


class OneLowerCaseExceptiom(Error):
    pass


class OneUpperCaseException(Error):
    pass


class OneDigitException(Error):
    pass


class OneSpecialCharError(Error):
    pass


class LoginError(Error):
    pass


class SignUp:
    def __init__(self, fn, ln, un, pwd):
        self.fn = fn
        self.un = un
        self.ln = ln
        self.pwd = pwd


class SignIn:
    def __init__(self, un, pwd):
        self.un = un
        self.pwd = pwd

    def loginCheck(self, signup):
        if self.un == signup.un and self.pwd == signup.pwd:
            return True
        else:
            return False


class Main:
    def __init__(self):
        fn = input("Enter first name")
        ln = input("Enter last name")
        un = input("Enter Username for account")
        lower = False
        upper = False
        digit = False
        special = False
        while True:
            try:
                pwd = input("Enter Password")
                if len(pwd) <= 8 and len(pwd) >= 16:
                    raise LengthException
                for i in pwd:
                    if i.islower():
                        lower = True
                if lower == False:
                    raise OneLowerCaseExceptiom
                for i in pwd:
                    if i.isupper():
                        upper = True
                if upper == False:
                    raise OneUpperCaseException
                for i in pwd:
                    if i.isdigit():
                        digit = True
                if digit == False:
                    raise OneDigitException
                for i in pwd:
                    if 33 <= ord(i) <= 64 or 91 <= ord(i) <=96 or 123 <= ord(i) <= 126:
                        special = True
                if not special:
                    raise OneSpecialCharError
                break

            except LengthException:
                print("Length of password must be greater than 8 & less than 16" + "\n")

            except OneLowerCaseExceptiom:
                print("There must be one lowercase character" + "\n")

            except OneUpperCaseException:
                print("There must be one upper case character, Try Again" + "\n")

            except OneDigitException:
                print("There must be one numeric character, try again" + "\n")
            except OneSpecialCharError:
                print("There must be one special character, try again" + "\n")
        try:
            signup = SignUp(fn, ln, un, pwd)
            signinun = input("Enter username for sign in")
            signinpwd = input("Enter password for signin")
            signin = SignIn(signinun, signinpwd)
            check = signin.loginCheck(signup)
            if check:
                print("Successfully signed in")
            else:
                raise LoginError

        except LoginError:
            print("Invalid Username or Password")
            exit()


obj = Main()