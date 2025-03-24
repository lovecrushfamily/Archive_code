# Importing necessary modules
import sys  # Provides access to some variables used or maintained by the interpreter
import os.path  # Provides a way of using operating system dependent functionality like reading or writing to the file system
import argparse  # Makes it easy to write user-friendly command-line interfaces

def main():
    # Print the name of the file and its relative path
    print("\nFile name: " + os.path.basename(__file__))
    print("Relative path: " + __file__ +"\n"+  "*"* 50 +  '\n')

    # Check if there are any command-line arguments
    if len(sys.argv) == 1:
        print("No arguments found")
    else:
        print("Arguments found:")
        
        # Create the parser
        parser = argparse.ArgumentParser(description="Process some integers.")
        
        # Add positional arguments
        parser.add_argument("arg_pos1", type=str, help="First positional argument")
        parser.add_argument("arg_pos2", type=str, help="Second positional argument")
        parser.add_argument("arg_pos3", type=int, help="Third positional argument")

        # Add optional arguments with flags
        parser.add_argument("-a", "--age", type=int, help="Optional argument for age")
        parser.add_argument("-c", "--class", type=int, help="Optional argument for class")

        # Parse the arguments
        args = parser.parse_args()

        # Print the parsed arguments
        for arg in vars(args):
            print(f"{arg}: {getattr(args, arg)}")

# Check if the script is being run directly (not imported as a module) and call the main function
if __name__ == "__main__":
    main()