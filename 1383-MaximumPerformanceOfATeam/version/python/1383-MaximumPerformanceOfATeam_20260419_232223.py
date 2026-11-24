# Last updated: 4/19/2026, 11:22:23 PM
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        # MOD = 10**9 + 7

        # speed_sorted_index = sorted(range(n), key = lambda x: speed[x])
        # efficiency_sorted_index = sorted(range(n), key = lambda x: efficiency[x])

        # # speed_sorted_index_dict = {}
        # # for i, key in enumerate(speed_sorted_index):
        # #     speed_sorted_index_dict[key] = i

        # productions = []
        # for i in range(n):

        #     ind = efficiency_sorted_index[i]
            
        #     min_efficiency = efficiency[ind] 
        #     min_efficiency_speed = speed[ind]

        #     index = speed_sorted_index.index(ind)
        #     # index = speed_sorted_index_dict[ind]

        #     del speed_sorted_index[index]
            
        #     sum_ = min_efficiency_speed

        #     m = k if i <= n-k else n-i
        #     for j in range(1, m):
        #         sum_ += speed[speed_sorted_index[-j]]

        #     production = sum_ * min_efficiency
            
        #     productions.append(production)

        # return max(productions) % MOD

        import heapq

        MOD = 10**9 + 7

        eng = sorted(zip(speed, efficiency), key=lambda x:x[1], reverse=True)

        productions = []
        heap_speed = []
        total_speed = 0

        for spd, eff in eng:

            total_speed += spd

            heapq.heappush(heap_speed, spd)

            if len(heap_speed) > k:
                total_speed -= heapq.heappop(heap_speed)

            production = total_speed * eff

            productions.append(production)

        return max(productions) % MOD


