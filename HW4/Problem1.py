#This is for CS362 OSU Hongyiel Suh
# problem  1
# find cube
def find_cube(user_input):
    the_cube = user_input * user_input * user_input
    return the_cube

# get input by user
def main():
    try:
        user_input = int(input("Please type what number do you want to expect: "))
        get_cube = find_cube(user_input)
        print(get_cube)
    except:
        print ("This is not a number")

# main

main()
