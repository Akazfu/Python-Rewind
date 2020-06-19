def cal_travese(input_str):
    input_list = input_str.split()
    postorder, inorder = input_list[0], input_list[1]
    root = postorder[-1]
    seen = set(root)
    result, ridx = [root], 0

    while len(result) < len(inorder):
        idx_in = inorder.index(root)
        idx_post = postorder.index(root)
        if idx_in-1 >= 0 and inorder[idx_in-1] not in seen:
            result.append(inorder[idx_in-1])
            seen.add(inorder[idx_in-1])
        if idx_post-1 >= 0 and postorder[idx_post-1] not in seen:
            result.append(postorder[idx_post-1])
            seen.add(postorder[idx_post-1])

        ridx += 1
        root = result[ridx]

    return ''.join(result)


input_str = 'FEBAKDC FEBCADK'
print(input_str)
print(cal_travese(input_str))
