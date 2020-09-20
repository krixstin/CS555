#!/usr/bin/env python3

VALID_2ND_POSITION_TOKENS = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS',
                             'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')
VALID_3RD_POSITION_TOKENS = ('INDI', 'FAM')


def detect_tokens(line):
    # determines tokens in a GEDCOM file line

    tokens = {}
    tokens["string"] = line

    split_line = line.split(" ", 2)

    tokens["level"] = split_line[0]

    if split_line[1] in VALID_2ND_POSITION_TOKENS:
        tokens["tag"] = split_line[1]
        tokens['args'] = split_line[2] if len(split_line) == 3 else ""
        tokens['valid'] = 'Y'
    elif split_line[2] in VALID_3RD_POSITION_TOKENS:
        tokens['args'] = split_line[1]
        tokens["tag"] = split_line[2]
        tokens['valid'] = 'Y'
    else:
        tokens["tag"] = split_line[1]
        tokens['args'] = split_line[2]
        tokens['valid'] = 'N'
    return tokens


def parse(dir):
    # opens a GEDCOM file and splits it by line

    parsed_file = []
    with open(dir, "r") as reader:
        content = reader.read().splitlines()

    for line in content:
        parsed_file.append(detect_tokens(line))
    return parsed_file


def project02(path):
    # satisfies the requirements for project02

    parsed_file = parse(path)

    for tokens in parsed_file:
        print(f"--> {tokens['string']}\n"
              f"<-- {tokens['level']}|{tokens['tag']}|{tokens['valid']}|{tokens['args']}")


def main():
    # run main code here

    project02("test.ged")


if __name__ == "__main__":
    main()
