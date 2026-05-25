class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) ==1:
            return int(tokens[0])
        calc = {
            "+":lambda a,b:a+b,
            "-":lambda a,b:b-a,
            "*":lambda a,b:a*b,
            "/":lambda a,b:int(float(b)/a)
        }
        nums=[]
        for c in tokens:
            if c in calc:
                print(nums)
                nums.append(calc[c](nums.pop(),nums.pop()))
                continue
            nums.append(int(c))
        
        return nums[0]