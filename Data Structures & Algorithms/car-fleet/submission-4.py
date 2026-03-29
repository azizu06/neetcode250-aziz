class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        s = []
        time = [0]*len(cars)
        for i in range(len(cars)):
            time[i] = (target - cars[i][0]) / cars[i][1]
        s.append(time[0])
        for i in range(1, len(time)):
            if time[i] > s[-1]:
                s.append(time[i])
        return len(s)

        

