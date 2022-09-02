import sys  
input = sys.stdin.readline

heap = ['']
n = int(input())
for i in range(n) : 
    e = int(input())
    if e == 0 : 
        if heap == [''] : 
            print(0)
        else : 
            e = heap[-1]
            heap[1], heap[-1] = heap[-1], heap[1]
            print(heap[-1])
            del heap[-1]
            index = 1
            while index * 2 < len(heap) : 
                a = index * 2
                if len(heap) == index * 2 + 1 : 
                    next = a
                else : 
                    b = a + 1
                    if heap[a] <= heap[b] : 
                        next = a
                    else : 
                        next = b
                if e > heap[next] : 
                    heap[index], heap[next] = heap[next], heap[index]
                    index = next
                else : 
                    break
    else : 
        heap.append(e)
        index = len(heap) - 1
        while index > 1 : 
            if e < heap[index//2] : 
                heap[index], heap[index//2] = heap[index//2], heap[index]
                index = index // 2
            else : 
                break