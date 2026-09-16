class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add the index to each value
        for i, t in enumerate(tasks):
            t.append(i)

        # sort by the first value so we can iterate through in order
        tasks.sort()

        res = []
        # this heap stores the tasks that are ready by processing time
        minHeap = []
        # i points to the next task we haven't added to the heap.
        # Start the clock when the first task arrives.
        i, time = 0, tasks[0][0]

        # untill we have processed all tasks & the heap is empty
        while minHeap or i < len(tasks):
            # Add every task that has arrived by the current time.
            # This includes tasks that arrived while the CPU was busy.
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            

            if not minHeap:
                # if the heap is empty, the cpu is idle
                # Jump to the next task's arrival time.
                # next loopadds it to heap
                time = tasks[i][0]
            else:
                # process the task with shortest time
                procTime, index = heapq.heappop(minHeap)
                # Advance the clock to when this task finishes.                
                time += procTime
                # append the index
                res.append(index)

        return res


        
        

        