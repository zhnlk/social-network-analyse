## 构造距离矩阵,网络距离矩阵
# 取出各机构名
def find_name(data,num):
    name = []
    for i in range(num):
        info_i = []
        for j in range(len(data[i])):
            info_i.append(data[i][j][4])
        name.append(info_i)
    return name
# 计算距离矩阵
def cul_matrix(name,num):
    matrix = np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            matrix[i][j]+=len(set(name[i]) & set(name[j]))
    return matrix
# 运行计算
num = len(data)
name = find_name(data,num)
matrix = cul_matrix(name,num)    

## 构造csv格式节点和边数据，使能导入gephi   
# 节点数据
id_1 = []
codes = []
for i in range(num):
    id_1.append(i) 
for i in range(num):
    codes.append(data[i][0][0])
df1 = pd.DataFrame({'Id':id_1, 'Label':codes})
path1 = 'C://Users//Administrator//Desktop//PC//nodes.csv'
df1.to_csv(path1, index=False, sep=',')
# 边数据
S,T,W = [],[],[]
for i in range(num):
    for j in range(i+1,num):
        if matrix[i][j] != 0:
            S.append(i)
            T.append(j)
            W.append(matrix[i][j])
id_2 = []
for i in range(len(S)):
    id_2.append(i) 
df2 = pd.DataFrame({'source':S, 'target':T, 'Id':id_2, 'weight':W})
path2 = 'C://Users//Administrator//Desktop//PC//edges.csv'
df2.to_csv(path2, index=False, sep=',')

## 影响力调整因子
path3 = 'C://Users//Administrator//Desktop//PC//result9_30.csv'
result = pd.read_csv(path3,error_bad_lines=False)
factor = []
adjusted_factor = []
for i in range(len(result)):
    rs = 0
    if result['sum'][i] != 0:
        s = result['sum'][i]
        r = result['ratio'][i]
        if s < 6:
            rs = r/(s*10)
        elif s > 5 and s < 11:
            rs = r/(s*5)
        else:
            rs = r/s
    factor.append(rs)
    adjusted_factor.append(rs*result['pageranks'][i])
df3 = pd.DataFrame({'factor':factor,'adjusted_factor':adjusted_factor})
path3 = 'C://Users//Administrator//Desktop//PC//factor.csv'
df3.to_csv(path3, index=False, sep=',')

## 或逻辑筛选
def ratio_value(data,ratio,value):
    data1 = []
    for i in range(len(data)):
        d = []
        for j in range(len(data[i])):
            if data[i][j][-1] != '' and data[i][j][10] != '':
                if float(data[i][j][-1]) >= ratio or float(data[i][j][10]) >= value:
                    d.append(data[i][j])
        data1.append(d)
    return data1
data = ratio_value(data,0.1,50000000)
