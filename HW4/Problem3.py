# CS362 OSU Hongyiel Suh
# problem  3
#Problem3

def get_name(First_name,Last_name):
    # Convert to dict
    return {"First_name":First_name,"Last_name":Last_name}

def main():
    # Get values
    First_name  = input("Give your First name: ")
    Last_name   = input("Give your Last name: ")
    # Before convert
    Full_name = get_name(First_name,Last_name)
    # After convert
    # Use Dict values from Full_name dict
    print(Full_name['First_name'] + Full_name['Last_name'])
    return 0
# if __name__ == '__main__':
main() # run the code
