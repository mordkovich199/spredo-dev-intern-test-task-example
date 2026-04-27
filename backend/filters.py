def filter_projects(projects):
    filtered = []

    for p in projects:
        if p["mcap"] <= 0:
            continue
        if not p["preview_listing"]:
            continue
        if p["max_supply"] != p["total_supply"]:
            continue
        if p["fdv"] >= 100000000:
            continue
        if p["volume_24h"] <= 50000:
            continue
        if p["tvl"] <= 50000:
            continue

        filtered.append(p)

    return filtered
