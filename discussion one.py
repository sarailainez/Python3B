""" Discusson 1:
A class to track and add boba drink orders per day.
"""

from dataclasses import dataclass


@dataclass
class BobaOrderTracker:

    day: str = "Monday"
    total_orders: int = 0

    def __str__(self) -> str:
        return (
            f"BobaOrderTracker(Day='{self.day}', "
            f"Total Orders={self.total_orders})"
        )

    def get_day(self) -> str:
        return self.day

    def set_day(self, new_day: str) -> None:
        if isinstance(new_day, str) and new_day.strip():
            self.day = new_day.strip()
        else:
            raise ValueError("Day must be a non-empty string.")

    def add_order(self, count: int) -> None:
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer.")
        self.total_orders += count

    def get_total_orders(self) -> int:
        return self.total_orders

    def reset_orders(self) -> None:
        self.total_order = 0
