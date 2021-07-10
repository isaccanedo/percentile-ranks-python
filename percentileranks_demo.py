import csv

import percentileranks


def main():

    """
    Test the percentileranks module with a set of
    exam grades from a CSV file.
    """

    print("--------------------")
    print("| Isac Canedo      |")
    print("| Percentile Ranks |")
    print("--------------------\n")

    try:

        f_in = open("grades.csv")
        r = csv.DictReader(f_in, fieldnames=['grade'])

        grades = []

        for item in r:
            grades.append(item['grade'])

        f_in.close()

        percentile_ranks = percentileranks.calculate_percentile_ranks(grades)

        percentileranks.print_percentile_ranks(percentile_ranks)

    except Exception as e:

        print(e)


main()
