"""
批量重命名
"""

import os

# 获取目标文件夹中的所有文件名
dir_path = r'Z:\tvshows\凡人修仙传 Fan Ren Xiu Xian Zhuan 2020 2160p WEB-DL H264.8bit AAC mp4\06-凡人修仙传-第5季星海飞驰篇'
file_list = os.listdir(dir_path)

delete_list = []
# 遍历文件列表
for file_name in file_list:
    if not file_name.endswith('.mp4'):
        delete_list.append(file_name)
        continue
    # 构建新的文件名，可以使用字符串的replace()函数或正则表达式替换
    new_file_name = file_name.replace('S06', 'S01')

    # 构建完整的文件路径
    old_file_path = os.path.join(dir_path, file_name)
    new_file_path = os.path.join(dir_path, new_file_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)


for delete_file in delete_list:
    path = os.path.join(dir_path, delete_file)
    os.remove(path)
