class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_count = {}
        have_count = 0
        window_count = {}
        for i in t:
            if i in need_count:
                need_count[i] += 1
            else:
                need_count[i] = 1
        retString = ""
        if s == t:
            return s
        if len(t)>len(s):
            return ""
        l = 0
        for r in range(len(s)):
            if s[r] in t:
                if s[r] not in window_count:
                    window_count[s[r]] = 0
                window_count[s[r]]+=1
                if window_count[s[r]] == need_count[s[r]]:
                    have_count += 1

            if len(need_count) == have_count:
                while len(need_count) == have_count:
                    if s[l] in need_count:
                        if len(s[l:r+1]) < len(retString) or retString == "":
                            retString = s[l:r+1]
                        window_count[s[l]] -= 1
                        if window_count[s[l]] < need_count[s[l]]:
                            have_count -= 1
                        l+=1
                    else:
                        l+=1

        return retString

