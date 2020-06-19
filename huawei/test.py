while  True:
    try:
        bin_num = str(bin(int(input())))[2:]
        count=0
        high=0
        print(bin_num)

        for cha in bin_num:
            if cha == '1':
                count += 1
            else:
                if count > high:
                    high=count
                count=0
        print(high)
    except:
        break
