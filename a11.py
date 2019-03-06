def char_mul(s): #a4v5h6
    char = ''
    num = ''
    for n in range(len(s)):
        
        while (s[n].isalpha()):
            char += s[n]
            temp = n
            while (s[temp].isdigit()):
                num += str(s[temp])
                temp += 1
                #num_f = int(num)
        print(char*num)    


inp = input()
char_mul(inp)
