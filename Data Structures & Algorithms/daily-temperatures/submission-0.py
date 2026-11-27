class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:  # 當 stack 非空且溫度大於 stack 裡的溫度時
                i = stack.pop()  # 取出溫度
                result[i] = index - i  # 寫入答案
            stack.append(index)
                
        return result