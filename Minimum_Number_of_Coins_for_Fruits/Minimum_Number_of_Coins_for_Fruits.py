class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        


#MEMOIZATION BASE (TIRADO DO EXEMPLO DO SLIDE)
#Input: n, s1,…,sn , f1,…,fn , v1,…,vn
#Sort jobs by finish times so that f1 f2 ... fn.
#Compute p(1), p(2), …, p(n)
#M[0] = 0
#for j = 1 to n
# M[j] = empty
#M-Compute-Opt(j) {
# if (M[j] is empty)
# M[j] = max(wj + M-Compute-Opt(p(j)), M-Compute-Opt(j-1))
# return M[j]
#}
