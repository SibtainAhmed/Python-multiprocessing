# import multiprocessing as mp

def doubleleList(lst):
    for i,v in enumerate(lst):
        lst[i] = v*3
    print(lst)

# if __name__ == '__main__':
#     with mp.Manager() as manager:
#         newRes = manager.list([0,1,2,3,4,5,6])
        
#         p2 = mp.Process(target=tripleList, args=(newRes,))
#         p2.start()
#         p2.join()

#     print(newRes)



# from multiprocessing import Process, Value, Array

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]

# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(9))

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print(num.value)
#     print(arr[:])