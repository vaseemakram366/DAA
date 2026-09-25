# Activity solutions


class Solution:
    def activitySelection(self, start, finish):
        activities = list(zip(start, finish))
        activities.sort(key=lambda x: x[1])

        count = 0
        last_finish = -1

        for s, f in activities:
            if s >= last_finish:
                count += 1
                last_finish = f

        return count

