# -*- coding: utf-8 -*-
from numpy import *
from matplotlib.pyplot import *

#### �T���v���f�[�^ ####

# �w�K�f�[�^�̐�
N = 50

# �P�ʉ~ x^2+y^2=1 �̓��ƊO��2�N���X�ɂ��Ă݂܂�
xs = []; ys = []; cs = []
for i in range(N):
    x = random.uniform(-1.5, 1.5)
    y = random.uniform(-1.5, 1.5)
    xs.append(x); ys.append(y)
    if x**2 + y**2 < 1:
        cs.append(0)
    else:
        cs.append(1)

scatter(xs, ys, c=cs, s=50, linewidth=0)
show()

savetxt("data1-8-3", [xs,ys,cs], delimiter="\t")
