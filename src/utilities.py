from pathlib import Path

def read_data(file_prefix: str) -> list[str]:
    """_summary_

    Args:
        file_prefix (str): File prefix in form of d{day number}p{puzzle number} ie d1p1

    Returns:
        list[str]: List of file lines, each represented by a string, with no newline characters
    """
    file_name = f"{file_prefix}.txt"
    file_path = Path("data") / file_name
    with open(file_path, "r") as file:
        return file.read().splitlines()