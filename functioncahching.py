import time
from functools import lru_cache
@lru_cache(maxsize=3)
def sum_work(n):
    time.sleep(n)
    return n  

if __name__ == '__main__':
    print("now running some work")
    sum_work(3)
    print("done......")
    sum_work(3)    
    print("called again")
    
    