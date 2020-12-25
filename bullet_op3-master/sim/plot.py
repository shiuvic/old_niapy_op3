import matplotlib.pyplot as plt
#----畫出圖-----
Al_list = ['ga','gwo','fpa','de','bat','pso']
for n in Al_list:
    Algorithm = n
    name = n
    x = 0
    n = []
    fname = 'C:/Users/shiuv/OneDrive/Desktop/data/data_mean/data_mean/%s.txt' % Algorithm
    with open(fname, 'r') as f:
        lines = f.readlines()  # 讀取所有行
        f.close()
    for i in range(20):
        n.append(float(lines[i]))
    plt.plot(n,label = name)
plt.legend()
plt.savefig('C:/Users/shiuv/OneDrive/Desktop/圖檔.png')
plt.show()
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')


# ----將5次資料為一單位平均-------
# Algorithm = 'pso'
# x = 0
# for i in range(50):
#     data_i = i
#     fname = 'C:/Users/shiuv/OneDrive/Desktop/data/%s/data(%s).txt' % (Algorithm,data_i)
#     with open(fname, 'r') as f:
#         lines = f.readlines()  # 讀取所有行
#         f.close()
#     for r in range(1,101,5):
#         for j in range(r,r+5,1):
#             x = x + float(lines[j])
#         file = 'C:/Users/shiuv/OneDrive/Desktop/data/data_mean/%s/data(%s).txt' % (Algorithm,data_i)
#         with open(file, 'a') as f:
#             f.write(str(x/5)+'\n')
#             f.close()
#         print(x/5)
#         x = 0
# -----將50次資料平均-----
# Algorithm = 'pso'
# x = 0
# for j in range(20):
#     for i in range(50):
#         data_i = i
#         fname = 'C:/Users/shiuv/OneDrive/Desktop/data/data_mean/%s/data(%s).txt' % (Algorithm,data_i)
#         with open(fname, 'r') as f:
#             lines = f.readlines()  # 讀取所有行
#             f.close()
#         x = x + float(lines[j])
#     print(x/50)
#     file = 'C:/Users/shiuv/OneDrive/Desktop/data/data_mean/data_mean/%s.txt' % Algorithm
#     with open(file, 'a') as f:
#         f.write(str(x/50)+'\n')
#         f.close()
#     x = 0

