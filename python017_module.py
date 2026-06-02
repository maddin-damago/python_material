def is_valid_password(password):
    #Return True if password is at least 8 characters and contains a digit.
    has_length = len(password) >= 8
    has_digit = any(c.isdigit() for c in password)  #any() prüft hier ob für irgendein Zeichen in password ein True für isdigit() herauskommt
    has_letter = any(c.isalpha() for c in password) #prüft ob Buchstaben
    has_upper = any(c.isupper() for c in password)  #prüft ob Großbuchstabe
    if has_length and has_digit and has_letter and has_upper:
        return True
    return False
 



class Auto:

    def __init__(self, name):
        self.name = name

    def fahre_los(self):
        print("Vroom vroom")

    def getName(self):
        return self.name