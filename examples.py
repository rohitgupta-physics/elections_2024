from poll_class import Poll, get_poll_ids


def main() -> None:

    # Print the latest 10 polls for the Presidential Race 2024
    print("Latest Ten Polls are:")
    poll_id_generator = get_poll_ids("general_election_biden_vs_trump_modified.csv")
    i = 0
    for poll_id in poll_id_generator:
        i += 1
        if i > 10:
            break
        print(Poll(poll_id, "general_election_biden_vs_trump_modified.csv"))
        print("-" * 30)

    # Print the starting and ending dates of the latest poll
    print("-" * 30)
    print("Latest poll included by FiveThirtyEight started on:")
    poll_id_generator = get_poll_ids("general_election_biden_vs_trump_modified.csv")
    poll_id = next(poll_id_generator)
    poll = Poll(poll_id, "general_election_biden_vs_trump_modified.csv")
    print("Starting date")
    print(poll.get_start_date())
    print("Ending date")
    print(poll.get_end_date())


if __name__ == "__main__":
    main()
