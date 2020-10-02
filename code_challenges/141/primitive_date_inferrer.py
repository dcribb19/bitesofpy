from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    date_strings = []
    sep = '-/.'
    c = Counter()

    formats = [_maybe_DateFormats(date) for date in dates]
    for date in formats:
        for d in date:
            c[d] += 1
    try:
        if c.most_common(2)[0][1] == c.most_common(2)[1][1]:
            raise InfDateFmtError
    except IndexError:
        pass

    dates = [date.replace(punct, '') for date in dates for punct in sep if punct in date]

    if c.most_common(1)[0][0] == DateFormat.NONPARSABLE:
        raise InfDateFmtError

    elif c.most_common(1)[0][0] == DateFormat.DDMMYY:
        for date in dates:
            try:
                date = datetime.strptime(date, '%d%m%y')
                date = date.strftime('%Y-%m-%d')
            except ValueError:
                date = 'Invalid'

            date_strings.append(date)

    elif c.most_common(1)[0][0] == DateFormat.MMDDYY:
        for date in dates:
            try:
                date = datetime.strptime(date, '%m%d%y')
                date = date.strftime('%Y-%m-%d')
            except ValueError:
                date = 'Invalid'

            date_strings.append(date)

    elif c.most_common(1)[0][0] == DateFormat.YYMMDD:
        for date in dates:
            try:
                date = datetime.strptime(date, '%y%m%d')
                date = date.strftime('%Y-%m-%d')
            except ValueError:
                date = 'Invalid'

            date_strings.append(date)

    else:
        for date in dates:
            if len(date) != 8:
                date = 'Invalid'
            try:
                date = datetime.strptime(date, '%d%m%Y')
                date = date.strftime('%Y-%m-%d')
            except ValueError:
                date = 'Invalid'

            date_strings.append(date)

    return date_strings
