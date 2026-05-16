class CountSquares:

    def __init__(self):
        self.pointCount=defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        x1,y1=point
        total=0

        for (x2,y2),count in self.pointCount.items():

            if x1==x2 or y1==y2:
                continue

            if abs(x2-x1) != abs(y2-y1):
                continue
            
            countCorner1=self.pointCount.get((x1,y2),0)
            countCorner2=self.pointCount.get((x2,y1),0)

            total+=count*countCorner1*countCorner2
        return total
            
            

        
