
#This is for CS362 OSU Hongyiel Suh
# problem  1
# find cube
def find_cube(user_input):
    if user_input != type(int):
        return user_input
    else:
        try:
            the_cube = user_input * user_input * user_input
            return the_cube
        except:
            return the_cube

# get input by user
def main():
    get_cube = find_cube(user_input)
    print(get_cube)

# main
# if __name__ == '__main__':
#     main()
