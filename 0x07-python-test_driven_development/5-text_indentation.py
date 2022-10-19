#!/usr/bin/python3
"""Function that prints a test with new lines.

"""





def text_indentation(text):

    """Method: prints a text with 2 new lines after given characters.

    Args:

    text(str): text

    Returns:

    No return

    """



    if not isinstance(text, str):

        raise TypeError("text must be a string")



    s = text[:]



    for d in ".?:":

        list_text = s.split(d)

        s = ""

        for i in list_text:

            i = i.strip(" ")

            s = i + d if s is "" else s + "\n\n" + i + d



    print(s[:-3], end="")
