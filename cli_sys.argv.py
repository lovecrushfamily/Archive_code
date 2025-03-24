import sys  # Import the sys module to access command-line arguments
import os.path  # Import the os.path module to manipulate file paths

def main():
    # Print the name of the file
    print("\nFile name: " + os.path.basename(__file__))
    # Print the relative path of the file
    print("Relative path: " + __file__ + '\n')

    # Check if there are no command-line arguments
    if len(sys.argv) == 1:
        print("No arguments found")
    else:
        print("Arguments found")
        # Iterate over the command-line arguments and print each one
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i}: {arg}")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
