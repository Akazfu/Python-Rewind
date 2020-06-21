input_ = [9, 3, 5]
sorted_ = input_[:]
sorted_.sort(reverse=True)
print(input_)
print(sorted_)
out_ = []
for i in input_:
    print(i)
    for idx, j in enumerate(sorted_):
        if i == j:
            print(j)
            out_.append(str(idx))
            sorted_[idx] = '$'
            break
print(','.join(out_))
