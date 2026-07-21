from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            res += str(len(string)) + "#" + string

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # 找到代表长度的数字后面的 #
            while s[j] != "#":
                j += 1

            # s[i:j] 是字符串长度
            length = int(s[i:j])

            # 字符串内容从 j + 1 开始
            start = j + 1
            end = start + length

            res.append(s[start:end])

            # 移动到下一个字符串的长度位置
            i = end

        return res