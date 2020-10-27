# coding = utf-8
import os
path = r"D:\\zh\\Documents\\GitHub\\MachineLearning\\Cplusplus\\source\\Test"


def conversion_coding(file_name, before='gbk', after='utf8'):
    # 此处转化文件编码，默认源文件编码为gbk，转换为utf8。
    # 原理： 读取文件中所有的内容（缓存到内存中），然后覆盖原文件（将缓存中的内容重新存入新文件）
    try:
        with open(file_name, 'r', encoding=before) as f:
            file_data = f.readlines()
        with open(file_name, 'w', encoding=after) as f:
            f.writelines(file_data)
    except Exception as e:
        print('转换文件“{0}”失败！:{1}'.format(file_name, e))


def get_file_name(dir_path):
    if os.path.isdir(dir_path):
        # 获取目录下所有的文件，此处可添加文件筛选规则，如后缀为txt的文件将被返回
        for file_name in os.listdir(dir_path):
            # 此处对文件进行筛选
            if file_name.split('.')[-1] == 'vtt':
                yield os.path.join(dir_path, file_name)
    else:
        print('"{0}" 这不是一个目录'.format(dir_path))


def main():
    path = input("请输入转换目录：")  # 取消注释可修改为根据输入的目录进行转换
    for file_name in get_file_name(path):
        conversion_coding(file_name)


main()
