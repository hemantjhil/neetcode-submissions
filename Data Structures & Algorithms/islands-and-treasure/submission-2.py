class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        
        """
        Fill each empty room with its distance from the nearest treasure chest.

        Values:
        - 0  -> treasure chest
        - -1 -> wall
        - INF -> empty room
        """

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        # Add all treasure chests as starting points.
        # This makes the BFS find the nearest chest for every room.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        def addRoom(r, c):
            # Ignore rooms that are outside the grid, already visited,
            # or blocked by a wall.
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                grid[r][c] == -1
            ):
                return

            # Add the valid room to the next BFS layer.
            q.append((r, c))
            visit.add((r, c))

        dist = 0

        # Process the grid level by level.
        # Every level represents rooms that are one step farther away.
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                # Store the shortest distance from a treasure chest.
                grid[r][c] = dist

                # Explore the four neighboring rooms.
                addRoom(r, c + 1)
                addRoom(r, c - 1)
                addRoom(r + 1, c)
                addRoom(r - 1, c)

            # Move to the next distance level.
            dist += 1