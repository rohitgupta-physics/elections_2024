import csv
import typing


class Pollster:

    def __init__(self, rating_id: str) -> None:
        self.rating_id: str = ""
        self._data: dict[str, str] = dict()
        file: typing.TextIO
        with open("pollster_rating.csv") as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                if row["pollster_rating_id"] == rating_id:
                    self.rating_id = rating_id
                    self._data = row
                    break
        if self.rating_id == "":
            raise ValueError("Not a valid pollster rating id")
        self.rating: str = self._data["numeric_grade"]
