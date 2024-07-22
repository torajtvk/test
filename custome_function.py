def jam(addad1: int, addad2: int):
    result = addad1 + addad2
    return result

def tafrigh(*args):
    print(args)

def sen(sal_tavalood: int=0, sal: int=1403):
    sen_find = sal - sal_tavalood
    return sen_find


tasht = jam("10", "20")
print(tasht)

tafrigh(10, 20, 15.5, "hello")
tafrigh(10)

sen_karbar = sen(1203)
print(sen_karbar)