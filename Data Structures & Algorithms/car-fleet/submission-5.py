class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        st = []
        for p, s in cars:
            st.append((target-p)/s)
            if len(st) >=2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)

        

