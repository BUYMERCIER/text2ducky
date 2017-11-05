################
#              # 
#  Text2ducky  #
#              #
################

import sys
import os

# main function
def main(input_file):
    if not os.path.isfile(input_file):
        # checks if the file exists
        print(input_file + " : file not found")
        return False
    # clears the previous inject.txt file if it exists
    if os.path.isfile("inject.txt"):
        os.system("rm inject.txt")
    
    f = open("inject.txt", "w")
    f.write("REM k4li \n\n")
    # opens the input file
    input_file_open = open(input_file, "r")
    for line in input_file_open:
        f.write("STRING " + line)
        f.write("ENTER\n")
    return True

# the program
if len(sys.argv) < 2:
    print("you need to specify an input file")
else:
    main(sys.argv[1])

