from itertools import combinations

class Dumbbell:
    def __init__(self, grip, disks):
        self.grip = grip
        self.disks = disks

    def configurations(self):
        weights = set()
        for i in range(0, len(self.disks) + 1):
            for conf in combinations(self.disks, i):
                weights.add(self.grip + 2 * sum(conf))
        return sorted(weights)

    def maxdelta(self):
        confs = self.configurations()
        return max((confs[i] - confs[i - 1] \
               for i in range(1, len(confs))))
