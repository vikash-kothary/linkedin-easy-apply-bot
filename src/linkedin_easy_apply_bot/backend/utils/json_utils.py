def data_to_json(file_path, data):
    """
    Write a dictionary to a JSON file.

    :param data: Dictionary to write to the file.
    :param file_path: Path to the JSON file.
    """
    import json
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json_from_file(file_path):
    """
    Read a JSON file and return its content as a dictionary.

    :param file_path: Path to the JSON file.
    :return: Dictionary containing the JSON data.
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f) if f.readable() else {}
    

def json_to_csv(file_path, data):
    """
    Convert a dictionary to a CSV file.

    :param data: Dictionary to convert to CSV.
    :param file_path: Path to the output CSV file.
    """
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8')
    