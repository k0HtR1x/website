

def str_counter (s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter +=1
        print(sym, counter)


str_counter('abcbaabcbababcbbaacabokkooacabko')




