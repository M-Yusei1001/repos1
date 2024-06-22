def check_num(num):
    if num >= 1 and num <= 10:
        return True
    else:
        return False
    
def into_int(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])