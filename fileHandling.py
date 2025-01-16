import os


# Read input file
class ReadFile:
    def __init__(self, option):
        
        self.__option = option
        self.__file_content = None
        self.__file_name = None
        self.read_file()


    def read_file(self):
        while True:
            file_name = input("\nPlease enter input file: ")

            # Check if file exists
            if os.path.exists(file_name):
                try:
                    with open(file_name, "r") as file:
                        content = file.read()
                    
                    if self._validate_content(content):
                        self._file_content = content
                        self._file_name = file_name
                        return 

                except IOError:
                    print("Error reading the file. Please resend the file again.")
            else:
                print("File does not exist. Please resend the file again.")

    # def _validate_content(self, content):
    #     # check whether option 1 and option 4 is valid
    #     if self._option == 1 or self._option == 4 or self._option == 5:
    #         if self.valid_content_symbol(content):
    #             return True
    #         else:
    #             print("File must only contain '*' or '.'. Please resend the file.")
    #             return False

    #     # check whether option 2 is valid
    #     elif self._option == 2 or self._option == 3:
    #         if self.valid_content_letter(content):
    #             return True
    #         else:
    #             print("File must only contain from A-Z and a-z only. Please resend the file.")
    #             return False
    #     else:
    #         return False


    # def valid_content_symbol(self, content):
    #     for letter in content:
    #         # Only * and . character are allow. However, newline or empty space should be allow too
    #         if letter not in ["*", ".", " ", "\n"]:
    #             return False
    #     return True
    
    # def valid_content_letter(self, content):
    #     # Only allow alphabet from A-Z and a-z. However, newline or empty space should be allow too
    #     for letter in content:
    #         if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n":
    #             return False
    #     return True
    
    def get_content(self):
        return self.__file_content # Get the file content safely
    
    def get_filename(self):
        return self.__file_name  # Return the file content safely