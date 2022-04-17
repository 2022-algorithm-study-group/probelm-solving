import argparse
import os
import shutil

CURRENT_PATH = os.path.dirname(__file__)
TEMPLATE_PATH = "{}/template".format(CURRENT_PATH)
PROBLEMLIST_PATH = "{}/problemlist".format(CURRENT_PATH)


def get_subject_and_urls_from_file(file_name):
    inputs = open("{}/{}".format(CURRENT_PATH, file_name), "r")
    lines = [line.replace("\n", "") for line in inputs.readlines()]
    inputs.close()
    return lines[0], lines[1:]


def create_problem_list_from_subject_and_urls(subject, urls):
    problemlist = open(PROBLEMLIST_PATH, "w+")
    problemlist.write("# {}\n".format(subject))
    for num, url in enumerate(urls):
        problemlist.writelines(
            "## {num}. [{name}]({url})\n".format(
                num=num + 1, name=_parse_name_from_url(url), url=url
            )
        )
    problemlist.close()


def create_template_from_urls(urls):
    if os.path.exists(TEMPLATE_PATH):
        shutil.rmtree(TEMPLATE_PATH, ignore_errors=True)
    os.mkdir(TEMPLATE_PATH)
    for num, url in enumerate(urls):
        p_name = (
            "{}.".format(num + 1)  # 문제번호
            + _parse_name_from_url(url)  # 문제이름
            + ".{}".format(FILE_TYPE)  # 파일타입
        )
        p_file = open("{}/{}".format(TEMPLATE_PATH, p_name), "w+")
        p_file.write("## {}".format(url))
        p_file.close()


def _parse_name_from_url(url):
    return "".join(url.split(URL_FORMAT))[:-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is a helper for generating problem templates"
    )
    parser.add_argument(
        "--input_file",
        "-i",
        type=str,
        default="input.txt",
        help="please input your input file's name. default file name is input.txt",
    )

    parser.add_argument(
        "--problem_origin_url",
        "-u",
        type=str,
        default="https://leetcode.com/problems/",
        help="please input problem's origin url. default origin url is https://leetcode.com/problems/",
    )
    parser.add_argument(
        "--file_type",
        "-t",
        type=str,
        default="py",
        help="please input code's file type. default file type is py",
    )

    args = parser.parse_args()
    URL_FORMAT = args.problem_origin_url
    FILE_TYPE = args.file_type
    INPUT_FILE_NAME = args.input_file
    subject, urls = get_subject_and_urls_from_file(INPUT_FILE_NAME)
    create_problem_list_from_subject_and_urls(subject, urls)
    create_template_from_urls(urls)
