from math import inf
from typing import List, TypeVar, Type, Union
from itertools import combinations
from dataclasses import dataclass


@dataclass
class DumbbellPlateItem:
    weight: float
    count: Union[int, float] = inf
    price: float = 0


class Dumbbell:
    def __init__(self, grip: float, plates: List[float] = None):
        self.grip = grip
        self.plates = plates if (plates is not None) else []

    def configurations(self) -> List[float]:
        weights = set()
        for i in range(0, len(self.plates) + 1):
            for conf in combinations(self.plates, i):
                weights.add(self.grip + 2 * sum(conf))
        return sorted(weights)

    def max_delta(self) -> float:
        confs = self.configurations()
        return max((confs[i] - confs[i - 1]
                   for i in range(1, len(confs))))

    def plates_weight(self) -> float:
        return 2 * sum(self.plates)

    def add_plate_pair(self, weight: float):
        self.plates.append(weight)

    DumbbellType = TypeVar("DumbbellType", bound="Dumbbell")

    @classmethod
    def calc_exact(cls: Type[DumbbellType], min_weight: float,
                   max_weight: float, max_delta: float) -> DumbbellType:
        dumbbell = cls(grip=min_weight)
        weight_range = max_weight - min_weight
        if weight_range <= 0:
            return dumbbell
        plate_weights = []
        power_of_2 = 0
        while dumbbell.plates_weight() < weight_range:
            new_plate = (2 ** (power_of_2 - 1)) * max_delta
            plate_weights.append(new_plate)
            power_of_2 += 1
        overhead = dumbbell.plates_weight() - weight_range
        if overhead >= 0:
            plate_weights[-1] -= (overhead / 2)
        return cls(grip=min_weight, plates=plate_weights)
