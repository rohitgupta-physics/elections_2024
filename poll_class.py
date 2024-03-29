import typing
import csv
from pollster_class import Pollster


class Poll:

    def __init__(self, poll_id: str) -> None:
        self.poll_id: str = ""
        self._data: dict[str, str]
        self.pollster: Pollster

        # checks if pollster id matches any of the pollster from general_election_biden_vs_trump.csv
        file: typing.TextIO
        with open("general_election_biden_vs_trump.csv") as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                if row["poll_id"] == poll_id:
                    self.poll_id = poll_id
                    self._data = row
                    self.pollster = Pollster(row["pollster_rating_id"])
                    break
        if self.poll_id == "":
            raise ValueError("Not a valid poll id")
