from typing import List


# 1 <= words.length <= 10^5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10^4
# puzzles[i].length == 7
# words[i] and puzzles[i] consist of lowercase English letters.
# Each puzzles[i] does not contain repeated characters.
# aa
# ab
# cd
class Node:
    def __init__(self, data=None):
        self.child = dict()
        self.data = data
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur_node = self.root
        for c in word:
            if c not in cur_node.child:
                cur_node.child[c] = Node(c)
            child = cur_node.child[c]
            cur_node = child
        cur_node.count += 1
        print()

    def getCount(self, word):
        cur_node = self.root
        count = 0
        for c in word:
            if c in cur_node.child:
                cur_node = cur_node.child[c]
                count += cur_node.count
            else:
                break
        return count


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # words for 돌면서 trie tree에 넣어주기 10**5 count ++ 하는 형식
        # puzzle -> 각 문자들 중복제거, sort 해주기
        words = ["".join(sorted("".join(set(word)))) for word in words]
        puzzles = ["".join(sorted("".join(set(puzzle)))) for puzzle in puzzles]

        trie = Trie()  # root node
        for word in words:
            trie.add(word)
        return [trie.getCount(p) for p in puzzles]


words = ["apple", "pleas", "please"]
puzzles = ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]
print(Solution().findNumOfValidWords(words, puzzles))
