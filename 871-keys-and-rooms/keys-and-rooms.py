class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()

        def visit(room):
            if room in visited:
                return 

            visited.add(room)

            for key in rooms[room]:
                visit(key)

        visit(0)

        return len(rooms)==len(visited)