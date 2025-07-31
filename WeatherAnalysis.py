def read_temperatures_from_file(filename):
    """
    TODO: Read float temperatures from the file and return as a list.
    Handle file not found error gracefully.
    """
    pass


def analyze_temperatures(temps):
    """
    TODO: Calculate max, min, and identify extreme temperatures 
    (above 34°C or below 30°C).
    Return a formatted report string.
    """
    pass


def main():
    filename = "temperatures.txt"  # Predefined input file
    temps = read_temperatures_from_file(filename)
    if temps:
        report = analyze_temperatures(temps)
        print(report)


if __name__ == "__main__":
    main()
