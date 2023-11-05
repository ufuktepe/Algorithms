import heapq


def furthest_building(heights, bricks, ladders):
	pq = []  # min-heap to store the climbs where we used ladders

	for i in range(1, len(heights)):
		climb = heights[i] - heights[i - 1]
		if climb <= 0:
			continue

		if ladders:
			# If there is an available ladder, use it
			heapq.heappush(pq, climb)  # O(
			ladders -= 1
		else:
			if pq and pq[0] < climb and bricks >= pq[0]:
				# Use a previously used ladder for the current climb and use bricks for pq[0]
				bricks -= heapq.heappop(pq)
				heapq.heappush(pq, climb)
			elif bricks >= climb:
				# Use bricks for the current climb
				bricks -= climb
			else:
				# Not enough bricks left
				return i - 1

	return len(heights) - 1

def test_1():
    heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks = 10
    ladders = 2
    furthest_building(heights, bricks, ladders) == 7