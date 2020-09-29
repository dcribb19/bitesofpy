def split_frames(frames: str) -> list:
    frames = frames.replace(' ', '')
    frames = (frame for frame in frames)

    split_frames = []

    while frames:
        if len(split_frames) == 9:
            split_frames.append(''.join(frames))
            break

        roll = next(frames)
        if roll == 'X':
            split_frames.append(roll)
        else:
            split_frames.append(''.join([roll, next(frames)]))

    return split_frames


def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    score = 0
    frames = split_frames(frames)

    for i, frame in enumerate(frames):
        # 10th Frame
        if i == 9:
            for roll in frame:
                if roll == '-':
                    continue
                elif roll == 'X':
                    score += 10
                elif roll == '/':
                    try:
                        score += 10 - int(frames[i][frames[i].index('/') - 1])
                    except ValueError:
                        score += 10
                else:
                    score += int(roll)
        # Frames 1-9
        else:
            for roll in frame:
                if roll == '-':
                    continue
                elif roll == 'X':
                    score += 10
                    # Bonus Rolls
                    try:
                        score += int(frames[i + 1][0])
                    except ValueError:
                        if frames[i + 1][0] == 'X':
                            score += 10
                            if i == 8:
                                try:
                                    score += int(frames[i + 1][1])
                                except ValueError:
                                    if frames[i + 1][1] == 'X':
                                        score += 10
                                    if frames[i + 1][1] == '/':
                                        try:
                                            score += 10 - int(frames[i + 1][0])
                                        except ValueError:
                                            score += 10
                            else:
                                try:
                                    score += int(frames[i + 2][0])
                                except ValueError:
                                    if frames[i + 2][0] == 'X':
                                        score += 10
                            continue
                    try:
                        score += int(frames[i + 1][1])
                    except ValueError:
                        if frames[i + 1][1] == '/':
                            try:
                                score += 10 - int(frames[i + 1][0])
                            except ValueError:
                                score += 10
                elif roll == '/':
                    try:
                        score += 10 - int(frames[i][0])
                    except ValueError:
                        score += 10
                    # Bonus Roll
                    try:
                        score += int(frames[i + 1][0])
                    except ValueError:
                        if frames[i + 1][0] == 'X':
                            score += 10
                else:
                    score += int(roll)
    return score
