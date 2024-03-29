import typing
import csv
from pollster_class import Pollster


class Poll:

    def __init__(self, new_poll_id: str, file_name: str) -> None:

        if not file_name.endswith("modified.csv"):
            raise ValueError("Not a modified csv file")

        self.new_poll_id: str = ""
        self.data: list[dict[str, str]]
        self.pollster: Pollster

        # checks if pollster id matches any of the pollster from general_election_biden_vs_trump.csv
        file: typing.TextIO
        with open(file_name) as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                if row["new_poll_id"] == new_poll_id:
                    self.new_poll_id = new_poll_id
                    self.data.append(row)
                    self.pollster = Pollster(row["pollster_rating_id"])
        if self.new_poll_id == "":
            raise ValueError("Not a valid poll id")
