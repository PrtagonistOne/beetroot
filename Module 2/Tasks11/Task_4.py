class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg

        with open('logs.txt', 'a') as f:
            f.write(self.msg)


raise CustomException('Some Error\n')
