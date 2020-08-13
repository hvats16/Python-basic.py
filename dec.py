def dec1(func1):
    def har():
        print("Exexuting now")
        func1()
        print("Executed")
    return har


@dec1
def who_is_harshit():
    print("Harshit is a good coder")
    
# who_is_harshit = dec1(who_is_harshit)
who_is_harshit()