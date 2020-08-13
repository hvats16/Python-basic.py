def searcher():
    import time
    #some 4 sec time consuming task
    book = "This is book on coding"
    time.sleep(4)
    
    while(1):
        text = (yield)
        if text in book:
            print("your text in book")
        else:
            print("text is not in the book")
            
        
search = searcher()
next(search)
search.send("harshit")  
input("press any key")
search.send("coding")