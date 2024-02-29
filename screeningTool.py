import pandas as pd
import os
import time

output_BUG = 'output_BUG'
same_ids = []
need_ids = []
read_ex_name = input('输入解析的表格名')

# 读取xlsx表格
df = pd.read_excel(f'{read_ex_name}.xlsx')

def replaceLog(oldText):
    need = oldText.replace('@', '\n')
    return need


# 根据id获取对应的log字段
def get_log_by_id(id):
    log = df.loc[df['id'] == id, 'log'].values[0]
    return log


# 根据log获取对应的id字段
def get_same_data(log):
    id = df.loc[df['log'] == log, 'id'].values[0]
    return id


def contains_char_in_string(s, char):
    return char in s


def check_same_log(clog):
    for id in need_ids:
        nlog = get_log_by_id(id)
        if (nlog == clog):
            return True
    return False


# def find_duplicates(lst):
#     return [item for item in set(lst) if lst.count(item) > 1]

def main():
    for need_id in df.id:
        vlog = get_log_by_id(need_id)
        if (check_same_log(vlog) == False):
            need_ids.append(need_id)
            print(f'单号{need_id}')
        else:
            same_ids.append(need_id)
            print(f'\033[4;31;40m 过滤单号---------------{need_id} \033[0m')

    # for log in df.log:
    #     need_id = get_same_data(log)
    #     # if (same_id.count(need_id) == 0):
    #     if (check_same_log(log) == False):
    #         same_id.append(need_id)
    #         print(f'需完成单号{need_id}')
    #     else:
    #         print(f'过滤单号---------------{need_id}')

    print('筛选完成~~~~~')


    # 创建保存图片的文件夹（如果不存在）
    if not os.path.exists(output_BUG):
        os.makedirs(output_BUG)

    # for id in df.id:
    #     with open(f'./output_BUG/{id}.txt', "w", encoding='utf-8') as fp:
    #         log = get_log_by_id(id)
    #         log = replaceLog(log)
    #         fp.write(log)
    current_date = time.strftime("%Y-%m-%d", time.localtime())

    with open(f'./output_BUG/{current_date}.txt', "w", encoding='utf-8') as fp:
        # for id in df.id:
        for id in need_ids:
            title = f'单号为： {id}'
            log = get_log_by_id(id)
            log = f'{title} \n {replaceLog(log)} \n \n \n \n \n'
            fp.write(log)
            print(f'需完成单号{id}')

    print(f'\033[4;31;40m 过滤单号---------------{same_ids} \033[0m')
    print('文件完成写入~~~~~')
    # log:str = get_log_by_id(90456)
    # log = log.replace('@','\n')
    # print(log)


main()
