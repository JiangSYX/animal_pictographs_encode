""" .ape to target """

import os
import sys


def decode(CodeSet):
    
    # 读取.ape文件
    try: cpath = sys.argv[2]
    except IndexError: sys.exit()
    else: epath = cpath if os.path.isabs(cpath) \
                        else os.path.abspath(sys.argv[0]).replace(sys.argv[0], cpath)
    if epath[-4:] != ".ape": sys.exit()
    try: 
        with open(epath, encoding = "utf-8") as f_obj: f_list = f_obj.readlines()
    except FileNotFoundError: sys.exit()
    else: f_dict = {os.path.basename(epath): f_list}

    f_name = list(f_dict.keys())[0]

    # 删除每一行的换行符并转换为unicode列表
    unidict = dict([(f_name, 
        [[ord(char) for char in line] for line in 
            [line.rstrip("\n") for line in list(f_dict.values())[0]]])])

    # 根据CodeSet将每一行所转换出来的unicode列表解码成基础符
    keycdict = dict([(f_name, [])])
    for sublist in list(unidict.values())[0]:
        keyclist = []
        for unic in sublist:
            for basekey, unicset in CodeSet.items():
                if unic in unicset:
                    keyclist.append(basekey)
                    break
        keycdict[f_name].append(keyclist)

    # 将每一行的基础符列表转换为字符串再以"/"分隔为列表
    numdict = dict([(f_name, 
        [keystr.split("/") for keystr in 
            [''.join(sublist) for sublist in list(keycdict.values())[0]]])])

    # 将结果unicode列表解码成原本的值列表再转换为字符串
    resultdict = dict([(f_name, 
        ["".join(sublist) for sublist in 
            [[chr(int(unic)) for unic in numlist] for numlist in list(numdict.values())[0]]])])

    # 将结果列表的第一个元素作为文件名, 其他元素按行写入文件
    with open(epath.replace(f_name, list(resultdict.values())[0][0]), "w", encoding = "utf-8") as f_obj:
        f_obj.writelines(list(resultdict.values())[0][1:])

    # 在终端打印一条信息
    print("\n* end of decode\n")