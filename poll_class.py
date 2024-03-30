import typing
import csv
from pollster_class import Pollster


def get_poll_ids(csv_file: str) -> list[str]:
    """Generates a list of poll ids for use in Poll class

    Parameters
    ----------
    csv_file : str
        A csv file containing election polls. The name of the csv file must end with
        modified.csv

    Returns
    -------
    list[str]
        A list of valid poll ids

    Raises
    ------
    ValueError
        If the argument does not end with modified.csv
    """

    if not csv_file.endswith("modified.csv"):
        raise ValueError("Not a valid csv file")
    ans: list[str] = list()
    file: typing.TextIO
    with open(csv_file) as file:
        reader: csv.DictReader[str] = csv.DictReader(file)
        row: dict[str, str]
        for row in reader:
            if row["new_poll_id"] not in ans:
                ans.append(row["new_poll_id"])
    return ans


class Poll:
    """
    A class used to represent a poll. If there are multiple polling questions asked by a
    pollster they are treated as distinct polls.

    ...

    Attributes
    ----------
    new_poll_id: str
        A poll id used to identify the poll in the csv file
    filename: str
        A csv file that contains poll data whose name ends with modified.csv

    Methods
    -------
    get_pollster_name() -> str
        Returns the name of the pollster
    get_candidate_names() -> list[str]
        Returns the names of the candidates polled
    get_polling_numbers() -> dict[str, float]
        Returns a dictionary with candidate name as keys and their polling numbers as values
    """

    def __init__(self, new_poll_id: str, filename: str) -> None:

        if not filename.endswith("modified.csv"):
            raise ValueError("Not a modified csv file")

        self.new_poll_id: str = ""
        self._data: list[dict[str, str]] = list()
        self.pollster: Pollster

        # adds all the polling data that matches the given poll id and raised a ValueError if the poll id is not present in the csv file
        file: typing.TextIO
        with open(filename) as file:
            reader: csv.DictReader[str] = csv.DictReader(file)
            row: dict[str, str]
            for row in reader:
                if row["new_poll_id"] == new_poll_id:
                    self.new_poll_id = new_poll_id
                    self._data.append(row)
                    self.pollster = Pollster(row["pollster_rating_id"])
        if self.new_poll_id == "":
            raise ValueError("Not a valid poll id")

    def get_pollster_name(self) -> str:
        """Returns the name of the pollster from the pollster_rating.csv file

        Returns
        -------
        str
            Name of the pollster e.g. "The New York Times/Siena College"
        """

        return self.pollster.get_name()

    def get_candidate_names(self) -> list[str]:
        """List of candidate names which are included in poll

        Returns
        -------
        list[str]
            A list containing candidate names like ["Joe Biden", ...]
        """

        return [row["candidate_name"] for row in self._data]

    def get_polling_numbers(self) -> dict[str, float]:
        """Polling data corresponding to a given poll

        Returns
        -------
        dict[str, float]
            Eg {"Joe Biden": 42.0, "Donald Trump": 43.0}
        """

        ans: dict[str, float] = dict()
        row: dict[str, str]
        for row in self._data:
            ans[row["candidate_name"]] = float(row["pct"])
        return ans


if __name__ == "__main__":
    poll = Poll("865580", "general_election_biden_vs_trump_modified.csv")
    print(poll.get_polling_numbers())
    print(get_poll_ids("general_election_biden_vs_trump_modified.csv"))
