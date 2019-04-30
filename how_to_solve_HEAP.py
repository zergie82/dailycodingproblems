'''
return a new sorted merged list from K sorted lists, each with size N
'''

import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, lst_index, item_index = heapq.heappop(heap)

        merged_list.append(val)

        if item_index + 1 < len(lists[lst_index]):
            next_tuple = (
                lists[lst_index][item_index + 1],
                lst_index,
                item_index + 1
            )
	    heapq.heappush(heap, next_tuple)

    return merged_list

if __name__ == '__main__':
    l = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    print(merge(l))
