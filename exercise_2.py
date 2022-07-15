def bigger_Is_greater(w):
    w = list(w)
    i = len(w)-1
    while i>0 and w[i-1] >= w[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    j = len(w)-1
    while w[j] <= w[i-1]:
        j -= 1
    temp = w[j]
    w[j] = w[i-1]
    w[i-1] = temp
    s = ""
    for k in range(i):
        s += w[k]
    l1 = w[i:len(w)]
    for k in range(-1,-(len(l1)+1),-1):
        s += l1[k]
    return s

bigger_Is_greater('dcba')