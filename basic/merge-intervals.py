def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if merged[-1][1] >= start:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

# Example usage
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]  # Example intervals
    result = merge_intervals(intervals)
    print(f"Merged intervals: {result}")
