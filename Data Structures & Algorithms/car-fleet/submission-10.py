class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort()
        sarr = [(target-cars[i][0]) / cars[i][1] for i in range(len(cars))]
        print(sarr)
        fleet = []
        for i in range(len(sarr)-1,-1,-1):
            if fleet and  fleet[-1] >= sarr[i]:
                continue
            fleet.append(sarr[i])
        
        return len(fleet)
