import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1": [], "series_2" : [], "series_3": []}
        for row in reader:
            #data["series_1"].append(row["series_1"])
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_idx = i
        for num_idx in range(i + 1, len(numbers)):
            if numbers[min_idx] > numbers[num_idx]:
                min_idx = num_idx
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    print(numbers)
    return numbers


def main():
    numbers = read_data("numbers.csv")
    sorted_series = selection_sort(numbers["series_1"])


if __name__ == '__main__':
    main()
