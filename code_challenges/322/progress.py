from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if books_read >= books_goal:
        return True

    if not day_of_year:
        day_of_year = int(datetime.today().strftime('%j'))

    if books_read / books_goal >= day_of_year / 365:
        return True

    return False


if __name__ == '__main__':
    assert not ontrack_reading(60, 0, 3)
    assert not ontrack_reading(60, 0)
    assert ontrack_reading(60, 1, 3)
    assert ontrack_reading(10, 10, 365)
