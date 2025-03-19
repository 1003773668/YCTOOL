"""
批量删除nfo文件
"""

import os


def get_file_path(start_path):
    res = []
    file_list = os.listdir(start_path)
    # 遍历文件列表
    for file_name in file_list:
        file_path = os.path.join(start_path, file_name)
        if os.path.isdir(file_path):
            res.extend(get_file_path(file_path))
        elif not file_name.endswith('.mp4'):
            res.append(file_path)
            continue
    return res


if __name__ == '__main__':
    root_path = r'Z:\tvshows\蜡笔小新 Crayon Shinchan'
    r = get_file_path(root_path)
    for path in r:
        os.remove(path)


