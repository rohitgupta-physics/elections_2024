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


if __name__ == "__main__":
    main()
