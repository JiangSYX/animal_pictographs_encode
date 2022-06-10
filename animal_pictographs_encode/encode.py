""" target to .ape """

import os
import sys
import random


def encode(CodeSet, ecname):
    
    # 读取文件内容
    try: cpath = sys.argv[2]
    except IndexError: sys.exit()
    else: epath = cpath if os.path.isabs(cpath) \
                        else os.path.abspath(sys.argv[0]).replace(sys.argv[0], cpath)
    try: 
        with open(epath, encoding = "utf-8") as f_obj: f_list = f_obj.readlines()
    except FileNotFoundError: sys.exit()
    else: f_dict = {os.path.basename(epath): f_list}

    # 将文件每一行变成unicode列表
    unidict = {}
    for f_name, f_list in f_dict.items():
        unidict[f_name] = [[ord(char) for char in line] for line in f_list]
    
    # 将文件每一行的unicode列表变成"\"分隔的字符串序列
    strdict = {}
    for f_name, unilist in unidict.items():
        strdict[f_name] = ["/".join([str(unic) for unic in sublist]) for sublist in unilist]

    # 根据CodeSet将每一行的字符串序列转换为对应的unicode列表
    # 字符串序列的每一个字符都从CodeSet中对应的列表中随机选择一个编码值
    # 编码值是图像文字的unicode值, 对应的unicode列表代表了一行的内容
    codedict = {}
    for f_name, strlist in strdict.items():
        codedict[f_name] = [[random.choice(CodeSet[char]) for char in strline]\
                                                            for strline in strlist]

    # 将每一行的编码结果列表转换为utf-8格式的二进制串
    utf8dict = {}
    for f_name, codelist in codedict.items():
        utf8dict[f_name] = [[chr(unic).encode("utf-8") for unic in codeline]\
                                                    for codeline in codelist]
    
    # 根据ecname创建以二进制写入的文件并将每一个二进制串列表写入文件的每一行
    # 将目标文件名包括后缀名编码写入文件第一行
    tarname = [chr(unic).encode("utf-8") for unic in 
        [random.choice(CodeSet[eckey]) for eckey in 
            '/'.join([str(ord(char)) for char in list(utf8dict.keys())[0]])]]
    if ecname == True:
        uniname = ''.join([chr(unic) for unic in 
            [random.choice(CodeSet[eckey]) for eckey in 
                '/'.join([str(ord(char)) for char in 
                    os.path.splitext(list(utf8dict.keys())[0])[0]])]])
        with open(epath.replace(list(utf8dict.keys())[0], f"{uniname}.ape"), "wb") as f_obj:
            f_obj.writelines(tarname); f_obj.write("\n".encode("utf-8"))
            for blist in list(utf8dict.values())[0]:
                f_obj.writelines(blist); f_obj.write("\n".encode("utf-8"))
    elif ecname == False:
        with open(os.path.splitext(epath)[0] + ".ape", "wb") as f_obj:
            f_obj.writelines(tarname); f_obj.write("\n".encode("utf-8"))
            for blist in list(utf8dict.values())[0]:
                f_obj.writelines(blist); f_obj.write("\n".encode("utf-8"))

    # encode结束, 在终端打印消息
    print("\n* end of encode\n")