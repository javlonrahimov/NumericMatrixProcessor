def heading(title, level=1):
    if level >= 6:
        return "###### " + str(title)
    if 1 <= level < 6:
        return "#" * level + " " + str(title)
    else:
        return "# " + str(title)
