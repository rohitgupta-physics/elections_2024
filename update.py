import urllib.request


def update_data() -> None:
    general_election: str = (
        "https://projects.fivethirtyeight.com/polls-page/data/president_polls.csv"
    )
    retrieve_data(general_election, "general_election_biden_vs_trump.csv")
    pollster_rating: str = (
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/pollster-ratings/pollster-ratings-combined.csv"
    )
    retrieve_data(pollster_rating, "pollster_rating.csv")


def retrieve_data(url: str, output_file: str) -> None:
    try:
        urllib.request.urlretrieve(url, output_file)
    except IOError:
        print("Local file path does not exist")
