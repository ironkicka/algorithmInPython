tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]
# 末端のNodeは子が存在しないが、子が存在しないNodeであることを示すためにそれぞれに空配列を用意しておく必要がある
# 今回は7 ~ 14の8個分必要。

data = [0]
while len(data) > 0:
    pos = data.pop(0)
    print(pos,end=' ')
    for i in tree[pos]:
        data.append(i)
