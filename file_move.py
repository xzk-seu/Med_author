import os
import shutil
from multiprocessing import Pool


def copy_proc(s, d):
    try:
        shutil.copyfile(s, d)
        print(s)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    root_path = os.path.join("C:\\Users", "xzk09", "Desktop", 'Med_author_d&p')
    dest_path = os.path.join("C:\\Users", "xzk09", "Desktop", 'Medicine_Author_data&paper', 'data')
    count = 0
    pool = Pool(10)
    for i in range(60):
        s_path = os.path.join(root_path, 'data%d' % i)
        print(len(os.listdir(s_path)))
        for file in os.listdir(s_path):
            source = os.path.join(s_path, file)
            dest = os.path.join(dest_path, file)
            pool.apply_async(copy_proc, args=(source, dest))
    pool.close()
    pool.join()

    # shutil.copy('', '')

