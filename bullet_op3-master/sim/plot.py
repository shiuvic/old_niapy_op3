import matplotlib.pyplot as plt
for i in range(49):
    data_i = i
    fname = 'C://Users//Po Wei//PycharmProjects//niapy_op3//bullet_op3-master//sim//data//data(%s).txt'% data_i
    x = []
    f = open(fname,'r')
    for i in range(1):
        num = f.read().splitlines()
        x.extend(num)

    f.close()
    print(x)
    plt.plot(x)
    plt.show()