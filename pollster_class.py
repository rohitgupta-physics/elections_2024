import csv
import typing


class Pollster:

    def __init__(self, rating_id: str) -> None:
        _ids: list[str] = list()
        with open("pollster_rating.csv") as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                _ids.append(row["pollster_rating_id"])
        if rating_id not in _ids:
            raise ValueError("Not a valid pollster rating id")
        else:
            self.rating_id = rating_id

    def get_rating(self) -> str:
        file: typing.TextIO
        with open("pollster_rating.csv") as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                if row["pollster_rating_id"] == self.rating_id:
                    return row["numeric_grade"]
        return "Not a valid pollster"
