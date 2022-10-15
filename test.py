from gztools import *
tg = create_tiangan(0)
# print(tg)
dz = create_dizhi(1)
print(dz.get_canggan())
# print(dz.get_canggan().benqi)

for c in dz.get_canggan():
    print(c)