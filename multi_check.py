import os
import json


def check_data(task_id, t_list, model):
    # path = os.path.join(os.getcwd(), '%s%d' % (model, task_id))
    path = os.path.join("C:\\Users", "xzk09", "Desktop", 'Med_author_d&p', '%s%d' % (model, task_id))
    if not os.path.exists(path):
        os.makedirs(path)
    file_list = os.listdir(path)
    existing = set()
    if model == 'data':
        for file in file_list:
            existing.add(int(file.split('.')[0]))
    elif model == 'paper':
        for file in file_list:
            existing.add(int(file.split('_')[0]))
    else:
        print('MODEL ERROR!')
    remain = set(t_list) - existing

    len_ex = len(existing)
    len_re = len(remain)
    print('task %d %s: existing %d, remain %d'% (task_id, model, len_ex, len_re))
    return len_ex, len_re, remain


if __name__ == '__main__':
    # t_id = int(input('please input task id (0 for 0-9,1 for 10-19...): \n'))
    # t_id = t_id * 10

    count_ex_data = count_ex_paper = count_re_data = count_re_paper = 0
    remain_set = set()
    # for i in range(t_id, t_id + 10):
    for i in range(60):
        with open('MedTask%d' % i, 'r') as fr:
            total_list = json.load(fr)
            print('task %d is %d' % (i, len(total_list)))
            cd_data = check_data(i, total_list, 'data')
            count_ex_data += cd_data[0]
            count_re_data += cd_data[1]
            remain_set.update(cd_data[2])
            # cd_paper = check_data(i, total_list, 'paper')
            # count_ex_paper += cd_paper[0]
            # count_re_paper += cd_paper[1]
            print('--------------------------------------------------')

    print('task ALL %s: existing %d, remain %d' % ("data", count_ex_data, count_re_data))
    print('task ALL %s: existing %d, remain %d' % ("paper", count_ex_paper, count_re_paper))
    with open('data_remain', 'w') as fw:
        print(len(remain_set))
        json.dump(list(remain_set), fw)

    with open('data_remain.txt', 'w') as fw:
        for r in remain_set:
            fw.write(str(r)+'\n')
