import os
import shutil


def split_file(src_file_path, dst_file_path):
    dirs1 = os.listdir(src_file_path)
    print(dirs1)
    for line in dirs1:
        filename = line.strip('\n')
        name = filename[: -4]
        src_file_name = src_file_path + '/' + filename
        dst_file_name = dst_file_path + '/' + name + '/'
        print(src_file_name)
        print(dst_file_name)
        if not os.path.isfile(src_file_name):
            print("%s not exist !!!" % src_file_name)
        else:
            shutil.copy(src_file_name, dst_file_name)
            print("copy %s -->> %s" % (src_file_name, dst_file_name))


split_file('C:/Users/mcdull/Desktop/test/model', 'C:/Users/mcdull/Desktop/test/OTB100')
