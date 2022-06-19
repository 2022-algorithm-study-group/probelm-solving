## https://leetcode.com/problems/range-module/
# 1 <= left < right <= 10**9
# At most 10**4 calls will be made to addRange, queryRange, and removeRange.
# aproach using segment tree
# 합을 구하는게 아니라, 중간에 빠져나간놈이 있는지 체크하는거야
# 그렇다고 한다면 어떻게 하는게 좋을까
# add or remove 작업 => segmenttree를 통해서 range에속하는 범위 전부 업데이트 해주기 -> 10**9 불가능
# record를 쌓아 두는 수밖에 없다. record를 (10,1),(14,-1),(17,+1),(21,-1) 다음과 같이 정렬되게 쌓아두기 => ordered container 이용
# search 작업
# 처음부터 더해가면서 현재 지점에서 +인지 -인지 체크한다.
# 만약에 찾고자 하는 query range에 들어오는 값에 도달했을때 현재 지점에서 1보자 작다면 return false하고
# range를 벗어나게 되면 return true한다.
