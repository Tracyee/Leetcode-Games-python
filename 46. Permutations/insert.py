class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        tem = []
        n = len(nums)
        for i in range(1,n):
            for k in res:
                for j in range(len(k)+1):
                    k.insert(j,nums[i]) # 在索引为j的位置插入元素
                    tem.append(k[:])
                    k.pop(j) # 删除索引为j的元素
            res=tem
            tem=[]
        return res

    def permute2(self, nums):
        '''
        a more pythonic way
        '''
        permutations = [[]]

        for head in nums:
            permutations = [rest[:i]+[head]+rest[i:] for rest in permutations for i in range(len(rest)+1)]
            print(permutations)

        return permutations
