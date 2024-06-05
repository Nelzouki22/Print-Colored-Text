# ANSI escape codes for colors
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Example usage
print(colors.OKBLUE + "This is blue text." + colors.ENDC)
print(colors.OKGREEN + "This is green text." + colors.ENDC)
print(colors.WARNING + "This is a warning." + colors.ENDC)
print(colors.FAIL + "This is a fail." + colors.ENDC)

