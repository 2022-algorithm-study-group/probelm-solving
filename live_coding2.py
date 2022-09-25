'''
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

 

Example 1:

Input: s = "aabb"
Output: ["abba","baab"]
Example 2:

Input: s = "abc"
Output: []
 

Constraints:

1 <= s.length <= 16
s consists of only lowercase English letters.


TestCase 1:
Input: s = "aabb"
Output: ["abba","baab"]

TestCase 2:
Input: s = "abc"
output: []

approach1: bruteforce
모든 순열에 대해서 팰린드롬인지 전부 체크한다.
모든순열: 16! = 2*10^13 * 16

approach2: 
1. 한 문자종류를 제외하고, 모든 문자에 대해서 짝수로 존재해야한다.
2. 중심을 기준으로 대칭이여야한다.
3. 만약에 홀수인 문자의갯수가 2개이상이라면 요거는 팰린드롬이 될 수가 없다.
4. 홀수인 1개라면 가운데다가 박고, 왼, 오른쪽에 동일한 문자 구성으로 배치 하면 될것같다.
5. 한쪽만 배치하는경우만 생각해보면된다.
6. 
    8 8 => 8!
    7 1 7 => 7!
    total a:4, b:6
    a=2, b=3  7!, 8!*16  => (N/2)!*(N) + N + (N/2)!
    
    s에 대해서 전체문자열 카운팅
'''

def getAllPalindromicPermutation(s):
    count_dict = defaultdict(int)
    for c in s:
        count_dict[c] +=1
    
    odd_cnt = 0
    odd_char = ''
    for v in count_dict.values():
        if v%2 == 1:
            odd_cnt +=1
            odd_char = v
    if odd_cnt > 1:
        return []
    
    s = []
    for k, v in count_dict.items():
        if v%2 == 0:
            s += v*(k/2)
    permute = permutations(s)
    
    result = []
    for str in permute:
        result.append(str + odd_char + str.reverse())
    
    return result
