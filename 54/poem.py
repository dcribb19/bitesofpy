import textwrap

INDENTS = 4

wrapper = textwrap.TextWrapper()
wrapper.subsequent_indent = ' ' * INDENTS
wrapper.width=45

su = """
     To be, or not to be, that is the question:
     Whether 'tis nobler in the mind to suffer

     The slings and arrows of outrageous fortune,
     Or to take Arms against a Sea of troubles,
     """


ru = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    poem = textwrap.dedent(poem).strip()
    paragraphs = poem.split('\n\n')
    index = 0

    for paragraph in paragraphs:
        lines = paragraph.splitlines()
        while index < len(lines):
            if index == 0:
                print(lines[0])
                index += 1
            else:
                print(' ' * INDENTS + lines[index])
                index += 1
        index = 0
