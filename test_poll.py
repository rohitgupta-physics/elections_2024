import pytest
from poll_class import Poll, get_poll_ids

poll_id_generator = get_poll_ids("general_election_biden_vs_trump_modified.csv")
valid_poll_id = next(poll_id_generator)


def test_initialization():
    with pytest.raises(ValueError):
        Poll("not a valid poll id", "not_a_valid_filename_modified.csv")
    with pytest.raises(ValueError):
        Poll(valid_poll_id, "not_a_valid_filename_modified.csv")
    with pytest.raises(ValueError):
        Poll(valid_poll_id, "general_election_biden_vs_trump.csv")
