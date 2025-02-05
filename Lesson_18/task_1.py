import re

class User:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        # Regular expression for basic email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, self.email):
            raise ValueError(f"Invalid email address: {self.email}")
        else:
            print(f"Email address: {self.email} validated.")


try:
    #user = User("test-email.com")
    user = User("test@email.com")
except ValueError as e:
    print(e)


