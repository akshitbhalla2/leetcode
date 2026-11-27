# 875. Koko Eating Bananas

**Difficulty:** Medium<br>
[View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/)

---

Koko must finish all banana piles within `h` hours. Each hour she chooses one
pile and eats up to `k` bananas from it. Return the minimum integer eating
speed `k` that lets her finish in time.

**Example 1:**

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

**Example 2:**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

**Example 3:**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

**Constraints:**

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`
