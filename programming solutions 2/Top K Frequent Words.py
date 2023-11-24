class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={i:0 for i in words}
        for w in words:
            freq[w]+=1
        heap=[]
        
        for f in freq:
            heap.append((-freq[f],f))
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]
        
