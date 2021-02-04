#Average element in the list

def get_list(list):
    result = 0
    for x in list:
        try:
            if x is not str:
                result = x + result
        except:
            return print("Fail get result")

    result = result / len(list)
    return result
def main():
    list = [1,'c']
    get_f= get_list(list)
# main()
