################  Multiple inheritamce ############

class Dad:
    basketball =1 

class Son(Dad):
    Dance = 1
    def is_dance(self):
        return f"Yes i dance {self.Dance} no of times"


class GrandSon(Son):
    Dance = 6
    def is_dance(self):
        return f"Jackson yeah!!"  \
            f"Yes i dance {self.Dance} no of times"


Darry = Dad()
Larry = Son()
Harry = GrandSon()

print(Harry.is_dance())

print(Harry.Dance)
            

