import argparse
import os
import shutil

ROOT_PATH = os.path.dirname(__file__)


def get_subject_and_urls(file_name):
    inputs = open("{}/{}".format(ROOT_PATH, file_name), "r")
    lines = [line.replace("\n", "") for line in inputs.readlines()]
    inputs.close()
    return lines[0], lines[1:]


def create_problem_list(problem_list_path, urls, url_format):
    if os.path.exists(problem_list_path):
        shutil.rmtree(problem_list_path, ignore_errors=True)
    os.mkdir(problem_list_path)

    problemlist = open(
        "{}/{}".format(problem_list_path, "problemlist.md"), "w+")
    problemlist.write("# {}\n".format(subject))
    for num, url in enumerate(urls):
        problemlist.writelines(
            "## {num}. [{name}]({url})\n".format(
                num=num + 1, name=_parse_name_from_url(url, url_format), url=url
            )
        )
    problemlist.close()


def create_template(template_path, urls, url_format, file_type):
    if os.path.exists(template_path):
        shutil.rmtree(template_path, ignore_errors=True)
    os.mkdir(template_path)

    for num, url in enumerate(urls):
        p_name = (
            "{}.".format(num + 1)
            + _parse_name_from_url(url, url_format)
            + ".{}".format(file_type)
        )
        p_file = open("{}/{}".format(template_path, p_name), "w+")
        p_file.write("## {}".format(url))
        p_file.close()


def _parse_name_from_url(url, url_format):
    return "".join(url.split(url_format))[:-1]


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
    url_format = args.problem_origin_url
    file_type = args.file_type
    subject, urls = get_subject_and_urls(args.input_file)
    cur_path = "{}/{}".format(ROOT_PATH, subject)

    create_problem_list(
        problem_list_path=cur_path,
        urls=urls,
        url_format=url_format
    )

    create_template(
        template_path="{}/template".format(cur_path),
        urls=urls,
        url_format=url_format,
        file_type=args.file_type
    )
