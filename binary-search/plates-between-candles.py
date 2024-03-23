class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        # calc 3 prefix sums
        # no. all plates untils curr idx
        pf = []
        # no. plates till left candle
        pf_l = [-1] * len(s)
        # no. plates till right candle
        pf_r = [0] * len(s)

        plate_count = 0
        for char in s:
            pf.append(plate_count)
            if char == '*': plate_count += 1

        lc_ind = -1
        for i, char in enumerate(s):
            if char == '|': 
                lc_ind = i
            pf_l[i] = lc_ind

        rc_ind = inf
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char == '|':
                rc_ind = i
            pf_r[i] = rc_ind
        
        out = []
        # get queries results
        for (start, end) in queries:
            if pf_l[end] < start or pf_r[start] > end: no_plates = 0
            else: no_plates = pf[pf_l[end]] - pf[pf_r[start]]
            out.append(no_plates)
        return out