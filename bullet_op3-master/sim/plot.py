import matplotlib.pyplot as plt
for i in range(19):
    data_i = i
    fname = 'F://新增資料夾 (2)//bullet_op3-master//sim//data//data(%s).txt'% data_i
    x = []
    f = open(fname,'r')
    for i in range(1):
        num = f.read().splitlines()
        x.extend(num)

    f.close()
    # print(x)
    plt.plot(x)
    plt.show()