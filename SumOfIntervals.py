def sum_of_intervals(intervals):
    if not intervals:
        return 0

    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:
            # Overlapping intervals, merge them
            current_end = max(current_end, end)
        else:
            # No overlap, add the current interval to merged and start a new one
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    # Add the last interval
    merged.append((current_start, current_end))

    # Calculate the sum of lengths
    total = 0
    for start, end in merged:
        total += end - start

    return total
def sum_of_intervals0(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top = a
        if top < b: s, top = s+b-top, b
    return s
print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))

print(sum_of_intervals0([[1, 4], [7, 10], [3, 5]]))