
# CS362 OSU Hongyiel Suh
# problem  1
# find cube
def find_cube(user_input):
    # if user input is
    if type(user_input) == str:
        return user_input
    else:
    # Get Cube when user_input is Number type (int , float , double ...)
        the_cube = user_input * user_input * user_input
        return the_cube
# get input by user
def main():
##########  User Input  ################
    user_input = 4
#######################################
    get_cube = find_cube(user_input)
    print(get_cube)

# main
if __name__ == '__main__':
    main()
