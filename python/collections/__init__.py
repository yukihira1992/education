from .base import PriorityQueue


def priority_queue(impl='list', asc=True):
    from .priority_queue import (
        PriorityQueueByList,
        PriorityQueueByOrderedList,
        PriorityQueueByHeap,
    )
    if impl == 'list':
        return PriorityQueueByList(asc)
    elif impl == 'ordered_list':
        return PriorityQueueByOrderedList(asc)
    elif impl == 'heap':
        return PriorityQueueByHeap(asc)
