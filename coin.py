from pwn import *
import re
import sys
 
p = re.compile("N=(\d+) C=(\d+)")
 
def range_sum(begin, end):
        query = ' '.join(str(i) for i in range(begin, end))
         
        conn.writeline(query)
        res = conn.readline()
         
        if res.find('Correct!') != -1 or int(res) == 9:
            while res.find('Correct!') == -1:
                conn.writeline(query)
                res = conn.readline()
             
            sys.stdout.write(res)
            return -1
         
        return int(res)
 
def find_counterfeit(begin, end):
     
    if begin + 1 == end:
        range_sum(begin, end)
        return -1
         
    mid = (begin + end) >> 1
     
    left_sum = range_sum(begin, mid)
     
    if left_sum == -1: return
     
    if left_sum != (mid - begin) * 10:
        find_counterfeit(begin, mid)
    else:
        find_counterfeit(mid, end)
 
 
if __name__ == '__main__':
    conn = remote('localhost', 9007)
    conn.read()
 
    sleep(4)
         
    while True:
        info = conn.readline()     
        m = p.search(info)
         
        if info == 'Congrats! get your flag\n':        
            sys.stdout.write(info + conn.read())
            break
         
        N = int(m.group(1))
         
        find_counterfeit(0, N)