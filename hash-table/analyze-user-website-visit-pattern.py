class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # sort by timestamp
        orig_t2ind = {timestamp[i]: i for i in range(len(timestamp))}
        timestamp = sorted(timestamp)
        sorted_ind = [orig_t2ind[t] for t in timestamp]
        print(sorted_ind)
        username = [username[ind] for ind in sorted_ind]
        website = [website[ind] for ind in sorted_ind]
        
        pattern_p_user = defaultdict(list)
        for i in range(len(username)):
            pattern_p_user[username[i]].append(website[i])
        
        pattern_scores = defaultdict(int)
        for pattern_list in pattern_p_user.values():
            for pattern in set(combinations(pattern_list, 3)):
                pattern_scores['_'.join(pattern)] += 1
        
        min_heap = []
        for pt, sc in pattern_scores.items():
            heapq.heappush(min_heap, (-sc, pt))
        out = heapq.heappop(min_heap)[-1]

        return out.split('_')