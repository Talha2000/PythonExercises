class CustomException(Exception):
    """Custom Exception
    
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

my_int = int(input())

try:
    if my_int < 10:
        raise CustomException("Input is less than 10")
    elif my_int > 10:
        raise CustomException("Input is greater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)

