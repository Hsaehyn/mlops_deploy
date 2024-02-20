# the code to handle any exception or error
import sys
import logging
from logger import logging

# the sys in "error_detail:sys" means this params is found in sys, it is of "sys" type
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,
        exc_tb.tb_lineno,
        str(error)
    )
    return error_message

    
# let's write a custom Exception case handler calss for our application
# this class will inhereit from the "Exception" class
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message) # initialize that we inhereit from the error message
        self.error_message = error_message_detail(error_message, error_detail=error_details)
        
    def __str__(self):
        return self.error_message

        
# if __name__ == "__main__":
#     try:
#         a = 1/0  # try with a case that is definite to generate an error
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e, sys)
        
        