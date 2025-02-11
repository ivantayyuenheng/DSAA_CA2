# Read output file
class OutputFile:
    def __init__(self):

        self.__outputfile = self.get_filename()

    def get_filename(self):
        while True:
            # Ask user for output file
            output = input("Please enter output file: ")

            # Check if the output file ends with .txt
            if output.endswith(".txt"):
                return output
            else:
                print("Output file can only end with txt. Please try again.")

    def send_file(self, content):
        
        # Write the content to the output file
        if self.__outputfile:  
            try:
                with open(self.__outputfile, "w") as file:
                    file.write(content)
            except IOError:
                print("Error creating output file.")
        else:
            print("No valid output file")

    # Get the output file namem
    def get_output_file_name(self):
        return self.__outputfile
    
