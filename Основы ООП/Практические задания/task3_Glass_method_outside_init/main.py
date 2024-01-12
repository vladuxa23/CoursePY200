from typing import Union


class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

        self.check_input_values()

    def init_capacity_volume(self, capacity_volume) -> None:
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError(f"Для capacity_volume ожидается int|float, получен {type(capacity_volume)}")
        if capacity_volume <= 0:
            raise ValueError("Значение capacity_volume должно быть больше 0")

        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume) -> None:
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError(f"Для occupied_volume ожидается int|float, получен {type(occupied_volume)}")
        if occupied_volume <= 0:
            raise ValueError("Значение occupied_volume должно быть больше 0")

        self.occupied_volume = occupied_volume

    def check_input_values(self):
        if self.occupied_volume > self.capacity_volume:
            raise ValueError("Значение occupied_volume не может быть больше capacity_volume")


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.capacity_volume)
    print(glass1.occupied_volume)

