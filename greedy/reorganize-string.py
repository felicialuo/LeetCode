class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap  = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        # get max count
        max_count = 0
        for k, v in hashmap.items():
            if v > max_count: 
                max_count = v
                max_char = k
        if max_count > (len(s) + 1) // 2:
            return ''
        out = [''] * len(s)
        i = 0

        # place max char
        while hashmap[max_char] != 0:
            out[i] = max_char
            hashmap[max_char] -= 1
            i += 2

        # place rest char
        for char, count in hashmap.items():
            while count > 0:
                if i >= len(s): i = 1
                out[i] = char
                count -= 1
                i += 2

        return ''.join(out)