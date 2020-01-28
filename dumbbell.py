from itertools import combinations, takewhile

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

    def max_delta(self):
        confs = self.configurations()
        return max((confs[i] - confs[i - 1]
               for i in range(1, len(confs))))

    @classmethod
    def calc_exact(cls, min_weight, max_weight, max_delta):
        weight_range = max_weight - min_weight
        weights = []
        if weight_range <= 0:
            return cls(grip=min_weight, disks=[])
        total_disks_weight = 0
        power_of_2 = 0
        while total_disks_weight < weight_range:
            new_weight = (2 ** (power_of_2 - 1)) * max_delta
            weights.append(new_weight)
            total_disks_weight += new_weight * 2
            power_of_2 += 1
        overhead = total_disks_weight - weight_range
        if overhead >= 1:
            weights[-1] -= (overhead / 2)
        return cls(grip=min_weight, disks=weights)
