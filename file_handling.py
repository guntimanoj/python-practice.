import os

FILENAME = "students.txt"


def write_records(filename, records):
    """Write a list of (name, score) tuples to file, one per line."""
    with open(filename, "w") as f:
        for name, score in records:
            f.write(f"{name},{score}\n")


def read_records(filename):
    """Read the file back into a list of (name, score) tuples."""
    records = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, score = line.split(",")
            records.append((name, int(score)))
    return records


def append_record(filename, name, score):
    """Append a single new record to the file."""
    with open(filename, "a") as f:
        f.write(f"{name},{score}\n")


def average_score(records):
    """Compute the average score from a list of (name, score) tuples."""
    if not records:
        return 0
    total = sum(score for _, score in records)
    return total / len(records)


if __name__ == "__main__":
    initial_data = [("Asha", 78), ("Ravi", 85), ("Meera", 91)]

    write_records(FILENAME, initial_data)
    print(f"Wrote {len(initial_data)} records to {FILENAME}")

    append_record(FILENAME, "Karan", 67)
    print("Appended one more record")

    records = read_records(FILENAME)
    print("All records:", records)
    print("Average score:", round(average_score(records), 2)) 
    
    os.remove(FILENAME)