# -*- coding: utf-8 -*-

""" 
apec.py
Animal Pictographs Encode Compiler | 动物图像文字编码编译器

Language: Python 3.8
MoreInfo: README.txt

"""

# 动物图像文字代码集, 10进制化16进制的unicode代码
headcode = "0x1f4{tc}"

tailcode = [f"0{num}" for num in range(0, 10)] + [f"0{chr(num)}" for num in range(65, 71)]
for dps in ((10, 20, "1"), (20, 30, "2"), (30, 40, "3")):
    tailcode.extend([str(num) for num in range(dps[0], dps[1])] + [dps[2] + f"{chr(num)}" for num in range(65, 71)])

sepccode = "0x1f495"

CodeSet = {}
for index, keyv in enumerate(list(range(0, 10)) + ["/"]):
    CodeSet[str(keyv)] = [
        int(headcode.format(tc = tc), 16) for tc in tailcode[(index*6): ((index+1)*6)]
    ]
    if index == 10: CodeSet[str(keyv)].append(int(sepccode, 16))


# 初始化apec
import sys

import x
import encode
import decode
import help
import version


# apec主函数
def main():
    try:
        cmd = sys.argv[1].lower()
        if cmd == "-x": task = "x"
        elif cmd in ["-e", "--encode"]: task = "encode"
        elif cmd in ["-i", "--icname"]: task = "icname"
        elif cmd in ["-d", "--decode"]: task = "decode"
        elif cmd in ["-h", "--help"]: task = "help"
        elif cmd in ["-v", "--version"]: task = "version"
        else: sys.exit()
    except IndexError: sys.exit()

    # 根据从命令行获取的参数执行任务
    if task == "x": exec(''.join([chr(xnum) for xnum in x.x]))
    elif task == "encode": encode.encode(CodeSet, ecname = False)
    elif task == "icname": encode.encode(CodeSet, ecname = True)
    elif task == "decode": decode.decode(CodeSet)
    elif task == "help": help.help()
    elif task == "version": version.version()


# 运行apec
if __name__ == "__main__":
    main()