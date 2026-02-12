import csv
def load_logs(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        return [row for row in reader]
