def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sum = 0
    running_mean = []
    for div_by, num in enumerate(sequence, start=1):
       sum += num
       mean = round(sum / div_by, 2)
       running_mean.append(mean)
    return running_mean
