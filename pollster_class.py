import csv
import typing


class Pollster:

    def __init__(self, rating_id: str) -> None:

        self.rating_id: str = ""
        self._data: dict[str, str] = dict()

        # checks if pollster rating id matches any of the pollster from pollster_rating.csv
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

        # if pollster rating is "NA", then we will treat it is 0
        try:
            self.rating: float = float(self._data["numeric_grade"])
        except ValueError:
            if self._data["numeric_grade"] == "NA":
                self.rating = 0
            else:
                raise ValueError(
                    f"Could not convert rating {self._data['numeric_grade']} into a float"
                )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pollster):
            return False
        return self.rating_id == other.rating_id

    def get_name(self) -> str:
        return self._data["pollster"]
