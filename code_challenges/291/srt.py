from datetime import datetime
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    data = []
    lines = text.splitlines()
    for line in lines:
        if line == '':
            continue
        elif line.isdigit():
            id = int(line)
        elif '-->' in line:
            start, end = line.split(' --> ')
            # get rid of microseconds
            start = start.split(',')[0]
            end = end.split(',')[0]

            timing = (datetime.strptime(end, '%H:%M:%S')
                      - datetime.strptime(start, '%H:%M:%S'))
        else:
            chars = len(line)
            data.append((id, chars / timing.seconds))
    data = sorted(data, key=lambda x: x[1], reverse=True)
    return [x[0] for x in data]
