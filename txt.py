import glob, os

path = 'c:\\Users\\Muwka\\PycharmProjects\\untitled2\\path\\txt'
pattern = '*.txt'

glob_path = os.path.join(path, pattern)
list_files = glob.glob(glob_path)
new_file = 'text.txt'

if list_files:
    i = 0
    array = [0, 0, 0]
    for file_name in list_files:
        with open(file_name, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
            for line in fr:
                array[i] += 1
        i += 1
    j = len(array)
    while j > 0:
        i = 0
        for file_name in list_files:
            with open(file_name, 'r', encoding='utf-8') as fr, open(new_file, 'a', encoding='utf-8') as fw:
                if i+1 == len(array):
                    if array[i] < array[0]:
                        fw.write('\n' + os.path.basename(file_name) + '\n')
                        for l in fr:
                            fw.write(l)
                        j -= 1
                        array[i] = 999
                else:
                    if array[i] < array[i+1]:
                        fw.write('\n' + os.path.basename(file_name) + '\n')
                        for l in fr:
                            fw.write(l)
                        j -= 1
                        array[i] = 999
            i += 1