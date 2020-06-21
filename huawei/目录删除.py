class Dir(object):
    def __init__(self, id):
        self.id = id
        self.child = []
        self.parent = None
# 检测指定id的dir是否已在列表中，如果是的话返回该对象，否则返回空


def get_dir(dirs, id):
    for dir in dirs:
        if dir.id == id:
            return dir
    return None
# 获取根节点（没有父亲的节点）


def get_root(dirs):
    for dir in dirs:
        if dir.parent is None:
            return dir
    return None
# 根据id删除结点的子节点（不必是直接子节点）


def delete_child(dir, child_id):
    child = get_dir(dir.child, child_id)
    if child is None:
        for d in dir.child:
            delete_child(d, child_id)
    else:
        dir.child.remove(child)
# 把输入的列表数据变成树结构


def generate_tree(ids):
    dirs = []
    for id in ids:
        cid, pid = id[0], id[1]
        cdir = get_dir(dirs, cid)
        if cdir is None:
            cdir = Dir(cid)
            dirs.append(cdir)
        pdir = get_dir(dirs, pid)
        if pdir is None:
            pdir = Dir(pid)
            dirs.append(pdir)
        # 把子节点加入父节点
        pdir.child.append(cdir)
        cdir.parent = pdir
    return dirs
# 获取子id列表


def get_child_id_list(dir, child_id_list):
    child_id_list.append(dir.id)
    if len(dir.child) != 0:
        for d in dir.child:
            get_child_id_list(d, child_id_list)


if __name__ == '__main__':
    ids = [[8, 6], [10, 8], [6, 0], [20, 8], [2, 6]]
    # 生成树结构
    dirs = generate_tree(ids)
    # 获取根节点
    root = get_root(dirs)
    # 升序输出
    child_ids = []
    get_child_id_list(root, child_ids)
    child_ids.sort()
    print(child_ids)
    # 删除指定目录的子节点
    delete_child(root, 8)
    # 升序输出
    child_ids = []
    get_child_id_list(root, child_ids)
    child_ids.sort()
    child_ids.remove(0)
    print(child_ids)
