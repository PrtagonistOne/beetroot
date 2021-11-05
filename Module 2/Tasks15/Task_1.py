import re


class Email:
    def __init__(self, email):
        self.email = Email.validate(email)

    @staticmethod
    def validate(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return email
        else:
            raise ValueError('Wrong email format')


usr1 = Email('playerdna4@gmail.com')
print(usr1.email, '\n')
usr2 = Email('llvl@0101/.com')
print(usr2)
