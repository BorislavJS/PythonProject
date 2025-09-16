def boarding_passengers(capacity, *groups):
    boarded = {}

    for group_size, program in groups:
        if capacity == 0:
            break
        if group_size <= capacity:
            boarded[program] = boarded.get(program, 0) + group_size
            capacity -= group_size

    sorted_boarding = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))

    result = ["Boarding details by benefit plan:"]
    for program, count in sorted_boarding:
        result.append(f"## {program}: {count} guests")

    total_boarded = sum(boarded.values())
    total_requested = sum(g[0] for g in groups)

    if total_boarded == total_requested:
        result.append("All passengers are successfully boarded!")
    elif capacity == 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)
