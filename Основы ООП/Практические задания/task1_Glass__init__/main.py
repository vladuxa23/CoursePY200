from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError(f"Для capacity_volume ожидается int|float, получен {type(capacity_volume)}")
        if capacity_volume <= 0:
            raise ValueError("Значение capacity_volume должно быть больше 0")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError(f"Для occupied_volume ожидается int|float, получен {type(occupied_volume)}")
        if occupied_volume <= 0:
            raise ValueError("Значение occupied_volume должно быть больше 0")

        if occupied_volume > capacity_volume:
            raise ValueError("Значение occupied_volume не может быть больше capacity_volume")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(capacity_volume=200, occupied_volume=100)
    glass_2 = Glass(capacity_volume=400, occupied_volume=300)

    print(glass_1.occupied_volume)
    print(glass_2.occupied_volume)
