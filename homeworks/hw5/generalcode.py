def read_file(file: str):
    d = []
    with open(f"{file}") as f:
        for line in f:
            split_line = line.replace("\n", "").split("|")
            d.append(split_line)
    return d
