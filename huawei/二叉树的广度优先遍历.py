input_str = 'DBEFCA DBAECF'
post_order, in_order = input_str.split()[0], input_str.split()[1]
root = post_order[-1]
idx_root = 0
bfs = [root]
seen = set(root)

while len(bfs) != len(post_order):
    idx_in = in_order.index(root)
    idx_post = post_order.index(root)
    if idx_in-1 >= 0 and in_order[idx_in-1] not in seen:
        bfs.append(in_order[idx_in-1])
        seen.add(in_order[idx_in-1])
    if idx_post-1 >= 0 and post_order[idx_post-1] not in seen:
        bfs.append(post_order[idx_post-1])
        seen.add(post_order[idx_post-1])
    idx_root += 1
    root = bfs[idx_root]
print(''.join(bfs))
