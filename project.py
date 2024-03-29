from update import update_data
from datetime import date, datetime


def main() -> None:
    update_data()
    with open("last_updated.txt", "w") as file:
        file.write(f"Data last retrieved on {date.today()} at {datetime.now()}")


if __name__ == "__main__":
    main()
