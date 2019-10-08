import random
import sys


def get_task_indexes():
    indices = set()
    while len(indices) < 25:
        index = random.randint(1, 100)
        indices.add(index)
    return list(indices)


def select_bingo_tasks(bingo_tasks):
    indices = get_task_indexes()
    tasks = []
    for index in indices:
        tasks.append(bingo_tasks[index])
    return tasks

task_list = []
with open('bingo_tasks_list.txt', encoding = "utf-8") as fp:
    for line in fp:
        task_list.append(line.rstrip())

head = ("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">\n"
        "<html lang=\"en\">\n<head>\n"
        "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        "<title>Bingo Cards</title>\n"
        "<style type=\"text/css\">\n"
        "\tbody { font-size: 12px; font-family: 'Verdana', sans-serif; }\n"
        "\ttable { margin: 40px auto; border-spacing: 2px; }\n"
        "\t.newpage { page-break-after:always; }\n"
        "\ttr { height: 60px; }\n"
        "\ttd { text-align: center; border: thin grey solid; border-radius: 15px; padding: 10px; width: 100px; height: 100px }\n"
        "</style>\n</head>\n<body>\n")

def generateTable(terms, pagebreak = True):
    """
    Generates an HTML table filled with terms to become
    the bingo card

    Parameters
    ----------
    terms : list
        a list of the terms to be put in the bingo card
    pagebreak : boolean
        a boolean variable to differentiate between two
        separate bingo cards. (Useful if trying to create
        more than one bingo card)

    Returns
    -------
    String
        A generated HTML string containing the HTML code for the table
    """
    ts = terms[:12] + ["WELCOME TO THE MKSM FAMILY!"] + terms[12:24]
    if pagebreak:
        res = "<table class=\"newpage\">\n"
    else:
        res = "<table>\n"
    for i, term in enumerate(ts):
        if i % 5 == 0:
            res += "\t<tr>\n"
        res += "\t\t<td>" + term + "</td>\n"
        if i % 5 == 4:
            res += "\t</tr>\n"
    res += "</table>\n"
    return res

out_file = open('card.html', 'w')
out_file.write(head)
cards = 1
for i in range(cards):
    terms = select_bingo_tasks(task_list)
    if i != cards - 1:
        out_file.write(generateTable(terms))
    else:
        out_file.write(generateTable(terms, False))
out_file.write("</body></html>")
out_file.close()
