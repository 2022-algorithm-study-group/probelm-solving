# 1week (라고 읽고 몇 주차인지 모름)

1. 인풋, 아웃풋 정의
2. 테스트케이스 대략 작성하면서 엣지 케이스 찾음
    - Array number input이면 정렬, empty, null, single entity 등 엣지케이스를 제시 후 디파인
3. 대략적인 풀이전략 설명 및 시간복잡도 제시
4. 수도코드 작성하면서 3)에서 말한거 맞는지 의견조율
5. 구현
6. 테스트하면서 디버깅
7. 팔로업
***

### by: 남규, solved: 홍준
### https://leetcode.com/problems/minimum-sideway-jumps/
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.

https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex1.png

Input: obstacles = [0,1,2,3,0]
Output: 2 
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).


```python
def solution(obstacles):
    n = len(obstacles)
    dp = [[n+1] * 3 for _ in range(n)]
    dp[0][0] = 1
    dp[0][1] = 0
    dp[0][2] = 1
    
    for stage in range(1, n):
        obs = obstacles[stage] - 1
        for i in range(3):
            if i == obs:
                dp[stage][i] = n
            elif dp[stage-1][i] < n:
                dp[stage][i] = dp[stage-1][i]
        minval = min(dp[stage])
        for i in range(3):
            if dp[stage][i] != n and (dp[stage][i] == n+1 or dp[stage][i] - minval > 1):
                dp[stage][i] = minval + 1
                
    print(dp)
    return min(dp[n-1])

print(solution([0,1,2,3,0]))



dp = [[float('inf')]*3 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 0
dp[0][2] = 1

for i in range(1, n):
    for j in range(3):
        if obstacle[i] == j:
            continue
        dp[i][j] = min(dp[i-1][j], dp[i-1][(j+1)%3]+1, dp[i-1][(j+2)%3]+1)
```

```c++
class Solution {
public:
    int minSideJumps(vector<int>& obstacles) {
        int n = obstacles.size() - 1;
        int dp[n][3];
        dp[0][1] = 0;
        dp[0][0] = dp[0][2] = 1;
        
        for(int i = 1; i < n; i++) {
            for(int j = 0; j < 3; j++) {
                if(obstacles[i] == j + 1 || obstacles[i + 1] == j + 1) {
                    dp[i][j] = n;
                } else {
                    dp[i][j] = min(dp[i - 1][j], min(dp[i - 1][(j + 2) % 3], dp[i - 1][(j + 1) % 3]) + 1);
                }
            }
        }
        
        return min(dp[n - 1][0], min(dp[n - 1][1], dp[n - 1][2]));
    }
};

// {{1, 0, 1}, {4, 0, 1}, {1, 4, 1}, {1, 2, 4}}

// {{1, 0, 1}, {4, 4, 1}, {2, 4, 4}, {2, 3, 4}}
```
***


### by: 홍준, solved: 남규, 홍준, 형준
### https://leetcode.com/problems/max-value-of-equation/

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

(yi + yj + xj - xi)

yj xj (yi-xi)



Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.


```python
class Solution:
  def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
    ans = -math.inf
    maxHeap = []  # (y - x, x)

    for x, y in points:
      while maxHeap and x + maxHeap[0][1] > k:
        heapq.heappop(maxHeap)
      if maxHeap:
        ans = max(ans, x + y - maxHeap[0][0])
      heapq.heappush(maxHeap, (x - y, -x))

    return ans
```










