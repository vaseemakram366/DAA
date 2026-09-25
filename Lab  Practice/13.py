# Job scheduling with deadlines

class Solution:
    def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x[2], reverse=True)

        max_deadline = max(job[1] for job in jobs)
        slots = [-1] * (max_deadline + 1)

        count = 0
        profit = 0

        for job_id, deadline, value in jobs:
            for slot in range(deadline, 0, -1):
                if slots[slot] == -1:
                    slots[slot] = job_id
                    count += 1
                    profit += value
                    break

        return count, profit