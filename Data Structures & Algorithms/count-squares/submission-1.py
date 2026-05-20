class CountSquares:

    def __init__(self):
        self.points=defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        x,y=point
        total=0
        for (x1,y1),count in self.points.items():
            if (x1==x or y1==y):
                continue
            
            if abs(x1-x)!=abs(y1-y):
                continue
            
            countCorner1=self.points.get((x,y1),0)
            countCorner2=self.points.get((x1,y),0)

            total+=count*countCorner1*countCorner2
        return total
        
