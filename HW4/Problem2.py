
# CS362 OSU Hongyiel Suh
# problem  2
#Average element in the list
def get_list(list):
    result = 0 # setting the initial value for get # result
    for x in list:
        # find list values
        try:
            # if value is number
            if x is not str:
                result = x + result
        except:
            # if value is not Number
            return print("Fail get result")
    # calculate if the results are passed
    result = result / len(list)
    return result
def main():
    # Example result list
    list = [1,'c']
    get_f= get_list(list)
# main()
