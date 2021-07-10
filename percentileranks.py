import collections
import math


def calculate_percentile_ranks(data):

    """
    Takes a list of numeric data and returns a
    list of dictionaries containing the discrete
    data values on order and their corresponding
    percentile ranks.
    Intermediate values are also included.
    """

    percentile_ranks = []

    frequencies = collections.Counter(data)
    frequencies = sorted(frequencies.items())

    count = len(data)

    cumulative_percentage = 0

    for item in frequencies:

        grade = int(item[0])
        frequency = int(item[1])
        percentage = frequency / count
        percentile_rank = cumulative_percentage
        cumulative_percentage += percentage

        percentile_ranks.append({"grade": grade,
                                 "frequency": frequency,
                                 "percentage": percentage,
                                 "cumulative_percentage": cumulative_percentage,
                                 "percentile_rank": percentile_rank})

    return percentile_ranks


def print_percentile_ranks(percentile_ranks):

    """
    Print the data structure from
    calculate_percentile_ranks
    in a table format
    """

    heading = "|Grade|Frequency|Percentage|Cumulative|Percentile Rank|"

    width = len(heading)

    print("-" * width)
    print(heading)
    print("-" * width)

    formatstring = "|{:5.0f}|{:9.0f}|{:9.2f}%|{:9.2f}%|{:15.0f}|"

    for row in percentile_ranks:

        print(formatstring.format(row["grade"],
                                  row["frequency"],
                                  row["percentage"] * 100,
                                  row["cumulative_percentage"] * 100,
                                  row["percentile_rank"] * 100))

    print("-" * width)
