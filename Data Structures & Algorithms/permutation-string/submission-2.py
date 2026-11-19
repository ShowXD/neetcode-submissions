class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1, count2 = {}, {}
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1  # 目標
            count2[s2[i]] = count2.get(s2[i], 0) + 1  # 初始化視窗

        for i in range(len(s2) - len(s1)):
            if count1 == count2:
                return True
            else:
                count2[s2[i+len(s1)]] = count2.get(s2[i+len(s1)], 0) + 1  # 將新抓到的字元加入
                count2[s2[i]] = count2.get(s2[i], 0) - 1  # 離開視窗的字元減少
            if count2[s2[i]] == 0:
                del count2[s2[i]]
        if count1 == count2:
                return True
        return False
        