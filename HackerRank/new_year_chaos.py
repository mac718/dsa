def minimumBribes(q):
    num_bribes = 0
    p1 = 1
    p2 = 2
    p3 = 3
    for i in range(len(q)):
        if q[i] == p1:
            p1 = p2
            p2 = p3
            p3 += 1
        elif q[i] == p2:
            num_bribes += 1
            p2 = p3
            p3 += 1
        elif q[i] == p3:
            num_bribes += 2
            p3 += 1
        else:
            print("Too chaotic")
            return
    print(num_bribes)