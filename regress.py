class RegressiData:
    number_of_columns = 0
    values_table = []
    columns_names = []
    columns_types = []
    columns_units = []
    columns_format = []
    columns_precision = []
    columns_significant_figures = []

    def __init__(self, path: str = None):
        """
        Import a regressi file with all of it's data.
        :param path: path to the file to import
        """
        if path is not None:
            if not valid_file(path):
                raise IOError("Invalid regressi file : Invalid header")

            self.number_of_columns, self.columns_names = generic_extractor(path, "NOM VAR")
            trash, self.columns_types = generic_extractor(path, "GENRE VAR")
            trash, self.columns_units = generic_extractor(path, "UNITE VAR")
            trash, self.columns_format = generic_extractor(path, "FORMAT VAR")
            trash, self.columns_precision = generic_extractor(path, "PRECISION VAR")
            trash, self.columns_significant_figures = generic_extractor(path, "SIGNIF VAR")

            self.values_table = columns_extractor(path, "VALEUR VAR")


def valid_file(path: str) -> bool:
    """
    Check if regressi file is valid
    :param path: path to the file to test
    :return: whether the file is valid or not
    """
    with open(path, 'r') as file:
        if file.readline() == "EVARISTE REGRESSI WINDOWS 1.0":
            return False
        else:
            return True


def section_extractor(path: str, section_name: str) -> [str]:
    """
    Extract the lines within sections matching the keyword.
    Each matching section end with a none.
    If section is 0 line long, a \'\' will be place instead.
    :param path: Path to the file from whom data has to be extracted
    :param section_name: Keyword that has to be matched
    :return: The extracted data
    """

    text = []

    with open(path, 'r') as file:
        for l1 in file:
            if l1[0] in "£&" and section_name in l1:
                size = int(l1.split()[0][1:])
                if size == 0:
                    text.append('')
                else:
                    for i in range(size):
                        text.append(file.readline())
                text.append(None)

        return text[:-1]


def generic_extractor(path: str, keyword: str) -> (int, list):
    """
    Extract a list of elements from a section in a practical fashion
    :param path: Path to the file whom specified fields have to be extracted
    :param keyword: Keyword indicating the section to be extracted
    :return: The number of elements, followed by the elements, arranged in a list
    """
    elements = []

    lines = section_extractor(path, keyword)

    # sanity check
    if None in lines:
        raise IOError("Invalid regressi file : Multiples sections matches the \"" + keyword + "\" title")

    for element in lines:
        elements.append(element.strip())

    return len(elements), elements


def columns_extractor(path: str, keyword: str) -> list:
    """
    Extract the numerical data from the file
    :param path: Path to the file whom data shall be harvested
    :param keyword: Keyword indicating the section to be extracted
    :return: The data, organized in a 2D list. First the columns, then the lines.
    """
    raw = section_extractor(path, keyword)

    if None in raw:
        raise IOError("Invalid regressi file : Multiples \"" + keyword + "\" sections.")

    table = []

    for _ in raw[0].split():
        table.append([])

    for line in raw:
        sectioned_line = line.split()

        for column in range(len(table)):
            table[column].append(float(sectioned_line[column]))

    return table


def file_import(path: str) -> RegressiData:
    """
    Import a regressi file with all of it's data.
    :param path: path to the file to import
    :return: a regressi_data object, containing the same information as the file
    """

    data = RegressiData(path)
    return data
