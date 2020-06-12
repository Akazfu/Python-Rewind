import os
import os.path


def search_file(path_name, filename):
    os.chdir(path_name)  # 修改路径到top路径下
    for each_file in os.listdir(os.curdir):  # 将top路径下的文件生成列表
        if each_file == filename:  # 判断是否为目标文件
            print(os.getcwd()+os.sep+each_file)  # 如果是输出路径
        if os.path.isdir(each_file):  # 判断该文件是不是文件夹/目录
            search_file(each_file, filename)  # 进入到该文件夹下
            os.chdir(os.pardir)  # 若没有则返回上一层菜单


path_name = input('请输入top文件夹：')
filename = input('请输入要搜索的文件名字：')
search_file(path_name, filename)
