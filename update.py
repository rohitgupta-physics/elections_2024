import requests
import csv
import typing
from datetime import datetime, timezone


def update_data() -> None:

    general_election: str = (
        "https://projects.fivethirtyeight.com/polls-page/data/president_polls.csv"
    )
    retrieve_data(general_election, "general_election_biden_vs_trump.csv")
    create_new_pollid("general_election_biden_vs_trump.csv")

    pollster_rating: str = (
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/pollster-ratings/pollster-ratings-combined.csv"
    )
    retrieve_data(pollster_rating, "pollster_rating.csv")


def retrieve_data(url: str, output_file: str) -> None:
    print(f"Updating {output_file} ...")
    session = requests.Session()
    response = session.get(url, stream=True)
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
    with open("last_updated.txt", "r+") as update_file:
        content: str = update_file.read()
        update_file.seek(0)
        update_file.write(
            f"{output_file} updated at {datetime.now(timezone.utc)} UTC\n"
        )
        update_file.write(content)


def create_new_pollid(in_csv: str) -> None:
    out_name: str = in_csv.rstrip(".csv") + "_modified.csv"
    print(f"Updating {out_name} ...")

    in_file: typing.TextIO
    out_file: typing.TextIO
    with open(in_csv) as in_file:
        with open(out_name, "w", newline="") as out_file:
            in_reader: csv.DictReader[str] = csv.DictReader(in_file)
            out_writer = csv.writer(out_file)

            assert in_reader.fieldnames is not None
            in_headings: list[str] = list(in_reader.fieldnames)

            out_headings: list[str] = in_headings + ["new_poll_id"]
            out_writer.writerow(out_headings)

            current_index: int = -1
            current_poll_id: str = ""
            row: dict[str, str]
            for row in in_reader:
                if row["poll_id"] != current_poll_id:
                    current_index = 0
                    current_poll_id = row["poll_id"]
                else:
                    if row["answer"] == "Biden":
                        current_index += 1
                new_data: str = row["poll_id"] + str(current_index)
                new_row: list[str] = list(row.values()) + [new_data]
                out_writer.writerow(new_row)
