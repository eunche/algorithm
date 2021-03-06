import re
from typing import List

"""
Runtime: 44 ms
Memory: 14.5 MB
내 생각: 코드가 매우 복잡했고, 난해했다. 알고리즘 문제를 해결하기에 급급한 지저분한 코드였다.
>>1번풀이를 보고 보니, 코드가 유사했고 조건2개로 sort정렬하는걸 놓쳤다.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result_logs: List[str] = []
        original_logs: List[str] = logs[:]
        logs_items: list = []

        # (식별자, 데이터)로 리스트 생성
        for s in original_logs:
            splitted_log = s.split()
            log_item = [splitted_log.pop(0), ' '.join(splitted_log)]
            logs_items.append(log_item)

        let_list: list = []
        dig_list: list = []

        # 알파벳, 디지털 데이터에 따라 리스트를 구분해서 담는다.
        for log in logs_items:
            if "".join(log[1].split()).isalpha():
                let_list.append(log)
            elif "".join(log[1].split()).isdigit():
                dig_list.append(log)

        # 알파벳 데이터를 알고리즘 조건에 따라 정렬한다
        let_list.sort(key=lambda x: x[1])
        for i, let in enumerate(let_list):
            for j in range(i+1, len(let_list)):
                if let[1] == let_list[j][1]:
                    let_list[i][0], let_list[j][0] = let_list[j][0], let_list[i][0]

        result_logs = [" ".join(i) for i in let_list+dig_list]

        return result_logs


s = Solution()

input
print(s.reorderLogFiles(["a1 9 2 3 1", "g1 act car",
                         "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]))
