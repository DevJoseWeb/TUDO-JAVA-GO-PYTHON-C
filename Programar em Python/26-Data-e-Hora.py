# Programar em Python #26 - Data e Hora

from calendar import *;
from time import *;

# print(calendar(2016));
# print(month(2016, 7));
print(time());
print(localtime(time()));
print(asctime(localtime(time())));