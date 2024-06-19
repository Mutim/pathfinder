import os.path
from collections import deque
import time
import json


def pathing(graph, start, dest):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == dest:
            print(f"Node({node}) has reached it's Destination:")
            return [int(n) for n in path]

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]["connected_stands"]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


if __name__ == "__main__":
    t1 = time.time()
    with open('waypoints.json') as g:
        graph = json.load(g)
        for n1 in graph:
            for n2 in graph:
                # - Line will not take into account the added points as a shortcut to already generated paths
                # if os.path.exists(f'{n1}to{n2}.json'):
                #     continue
                path = pathing(graph, n1, n2)
                with open(f'{n1}to{n2}.json', 'w+') as f:
                    json.dump(path, f)

    length = time.time() - t1
    print(f'Finished! -- Operation took {int(length // 60)}:{int(length % 60):02} minutes')