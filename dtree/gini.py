import numpy as np


def list_str(li):
    return [f"{x:.2f}" for x in li]


def entropy(li):
    ent = 0
    for x in li:
        ent -= x * np.log(x)
    print("------")
    print(list_str(li), f", entropy={ent:.2f}")
    return ent


def gini(li):
    gn = 1
    for x in li:
        gn -= x ** 2
    print("------")
    print(list_str(li), f", gini={gn:.2f}")
    return gn


def dot_prod(li1, li2):
    s = 0
    for i in range(len(li1)):
        s += li1[i] * li2[i]
    print("------")
    print(list_str(li1))
    print(list_str(li2))
    print(f"dot_prod={s:.3f}")


def main():
    hot = [3. / 4, 1. / 4]
    med = [3. / 5, 2. / 5]
    cold = med
    # entropy([.999,.001])
    # gini([.999,.001])
    for li in [hot, med, cold]:
        entropy(li)
        gini(li)
    li1 = [4. / 14, 5. / 14, 5. / 14]
    li2 = [.37, .48, .48]
    dot_prod(li1, li2)
    li2 = [.56, .67, .67]
    dot_prod(li1, li2)
    entropy([9. / 14, 5. / 14])


main()
