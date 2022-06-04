## https://leetcode.com/problems/string-transforms-into-another-string/

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        conversion_mappings = dict()
        unique_characters_in_str2 = set()
        
        for letter1, letter2 in zip(str1, str2):
            if letter1 not in conversion_mappings:
                conversion_mappings[letter1] = letter2
                unique_characters_in_str2.add(letter2)
        # 현재 각 알파벳들이 바뀌어야할 상대 알파벳이 2개 이상이라면, 그러니까 str1에서는 같은 알파벳인데
        # str2에서는 다른 알파벳이라면 방법이 없으므로 False
            elif conversion_mappings[letter1] != letter2:
                return False
        
        # str1의 알파벳 개수가 26개라면 => str2의 알파벳 개수가 26개 미만이면
        # str1 알파벳 26개 중 몇 개는 분명 중복으로 str2의 같은 알파벳으로 대응될 것
        # 그러면 대응이 중복되는 (결국 같은 알파벳으로 바뀌어야할) str1의 알파벳 중 아무거나를
        # 대응이 중복되는 또 다른 알파벳으로 바꿈. 그러고나면 임시 저장 알파벳이 생기고,
        # 임시 저장 알파벳이 생기고 난 다음부터는 str1의 알파벳1을 str2의 알파벳2로 바꿀 때,
        # str1에 이미 있는 알파벳2를 임시 저장으로 바꾼다음 작업하면 바꾸기 가능
        # (대응관계는 동일함을 앞에서 검증했으므로)
        # str1 알파벳 개수가 26개 미만이면 애초에 임시 저장으로 쓸 알파벳이 존재하므로 어차피 True
        if len(unique_characters_in_str2) < 26:
            return True
        
        # str2의 알파벳 개수도 26개면 둘이 동일하지 않는 이상 불가능
        return False