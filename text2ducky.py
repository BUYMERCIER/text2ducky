################
#              #
#  Text2ducky  #
#              #
################

import sys
import os

# main function
def main(input_file):
    # help argument
    if input_file in ['-h', '--help', 'help']:
        print("Usage:\npython3 text2ducky.py [input_file]")
        return False

    if not os.path.isfile(input_file):
        # checks if the file exists
        print(input_file, ": file not found")
        return False
    # clears the previous inject.txt file if it exists
    if os.path.isfile("inject.txt"):
        os.system("rm inject.txt")

    with open("inject.txt", "w") as f:
        f.write("REM k4li \n\n")
        f.write("\nDELAY 1000\n\n") # 1 second of delay before starting typing
        # opens the input file
        input_file_open = open(input_file, "r")
        for line in input_file_open:
            f.write("STRING " + line)
            f.write("ENTER\nDELAY 50\n")
    return True

# the program
if len(sys.argv) < 2:
    print("you need to specify an input file")
else:
    main(sys.argv[1])

