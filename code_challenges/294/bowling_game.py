def split_frames(frames: str) -> list:
    '''Create a list of 10 frames.'''
    frames = frames.replace(' ', '')
    frames = (frame for frame in frames)

    split_frames = []

    while frames:
        if len(split_frames) == 9:
            split_frames.append(''.join(frames))
            break
        else:
            roll = next(frames)
            if roll == 'X':
                split_frames.append(roll)
            else:
                split_frames.append(''.join([roll, next(frames)]))
    return split_frames


def spare_roll(score, frames, i, st_bonus=False, *sp_bonus, **f_10):
    '''Calculate score if roll is a spare ('/').'''
    if st_bonus or sp_bonus:
        i += 1
    try:
        if f_10:
            # Spare can be either 2nd or 3rd roll.
            score += 10 - int(frames[i][frames[i].index('/') - 1])
        else:
            score += 10 - int(frames[i][0])
    except ValueError:
        score += 10
    return score


def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    score = 0
    frames = split_frames(frames)

    for i, frame in enumerate(frames):
        for roll in frame:
            # 10th Frame (i == 9)
            if i == 9:
                if roll == '-':
                    continue
                elif roll == 'X':
                    score += 10
                elif roll == '/':
                    score = spare_roll(score, frames, i, f_10=True)
                else:
                    score += int(roll)
            # Frames 1-9
            else:
                if roll == '-':
                    continue
                elif roll == 'X':
                    score += 10
                    # Bonus Rolls
                    b1 = frames[i + 1][0]
                    try:
                        score += int(b1)
                    except ValueError:
                        if b1 == 'X':
                            score += 10
                            # Strike in 9th Frame (i == 8) needs to look at
                            # 1st 2 rolls of 10th Frame
                            if i == 8:
                                b2 = frames[i + 1][1]
                                try:
                                    score += int(b2)
                                except ValueError:
                                    if b2 == 'X':
                                        score += 10
                                    if b2 == '/':
                                        score = spare_roll(
                                            score, frames, i, st_bonus=True
                                            )
                            else:
                                b2 = frames[i + 2][0]
                                try:
                                    score += int(b2)
                                except ValueError:
                                    if b2 == 'X':
                                        score += 10
                            continue
                    try:
                        score += int(frames[i + 1][1])
                    except ValueError:
                        if frames[i + 1][1] == '/':
                            score = spare_roll(score, frames, i, st_bonus=True)
                elif roll == '/':
                    score = spare_roll(score, frames, i)
                    # Bonus Roll
                    try:
                        score += int(frames[i + 1][0])
                    except ValueError:
                        if frames[i + 1][0] == 'X':
                            score += 10
                else:
                    score += int(roll)
    return score
