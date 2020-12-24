import warnings
warnings.filterwarnings("ignore", category=Warning)


Algorithm = 'fa'

def savefit(data_i, data,param):
    fname = 'C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//%s//data(%s).txt'% (Algorithm ,data_i)
    fval = 'C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//%s//best_val.txt'% Algorithm
    fbest = 'C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//%s//best_par.txt'% Algorithm
    with open(fname, 'r') as f:
        lines = f.readlines() #讀取所有行
        last_line = lines[-1]  # 取最後一行
        f.close()
    with open(fval, 'r') as f:
        best_val = f.read()
        print('bestval = ', best_val, '\nlast_line = ' , last_line)
        f.close()
    if(data < float(last_line)):
        with open(fname, 'a') as f:
            f.write('\n' + str(data))
            f.close()
    else:
        with open(fname, 'a') as f:
            f.write('\n' + last_line)
            f.close()
    if(float(data) < float(best_val)):
        with open(fbest, 'w') as f:
            f.write(str(param))
            f.close()
        with open(fval, 'w') as file:
            file.write(str(data))
            file.close()