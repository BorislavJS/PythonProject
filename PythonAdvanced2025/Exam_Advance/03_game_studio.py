def sort_games(*args, **kwarg):
    console_titles = set()
    pc_titles = set()

    for platform, title in args:
        if platform == "console":
            console_titles.add(title)
        elif platform == "pc":
            pc_titles.add(title)

    console_games = []
    pc_games = []

    for release_id, title in kwarg.items():
        release_date = "_".join(release_id.split("_")[:-1])
        entry = (release_id, release_date, title)
        if title in console_titles:
            console_games.append(entry)
        elif title in pc_titles:
            pc_games.append(entry)

    console_games.sort(key=lambda x: x[0])
    pc_games.sort(key=lambda x: x[0],reverse = True)

    result = []

    if console_games:
        result.append("Console Games:")
        for _, date, title in console_games:
            result.append(f">>>{date}: {title}")

    if pc_games:
        result.append("PC Games:")
        for _, date, title in pc_games:
            result.append(f"<<<{date}: {title}")

    return '\n'.join(result)

print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))