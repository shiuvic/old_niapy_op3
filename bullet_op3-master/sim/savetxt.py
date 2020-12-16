

def savefit(data_i, data):
    fname = 'C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//data(%s).txt'% data_i
    with open(fname, 'r') as f:
        lines = f.readlines() #讀取所有行
        last_line = lines[-1]  # 取最後一行
        f.close()
    if(data < float(last_line)):
        with open(fname, 'a') as f:
            f.write('\n' + str(data))
            f.close()
    else:
        with open(fname, 'a') as f:
            f.write('\n' + last_line)
            f.close()
