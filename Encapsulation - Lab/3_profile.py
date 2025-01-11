class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_long_enough = len(value) >= 8
        has_uppercase_letter = any([el for el in value if el.isupper()])
        has_digit = any([el for el in value if el.isdigit()])

        if not (is_long_enough and has_uppercase_letter and has_digit):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
