from __future__ import annotations
from typing import List

EOL_PUNCTUATION = ",.!?"


class Document:
    def __init__(self) -> None:
        self.lines: List[str] = []

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into
                the document. If None, the line is added at the end.
                Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if index is not None:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        line_1 = self.lines[index_one]
        line_2 = self.lines[index_two]
        self.lines[index_one] = line_2
        self.lines[index_two] = line_1

        return self

    def merge_lines(self, indices: List[int]) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row,
            the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        first_index = indices[0]
        lines_to_merge = [self.lines[index] for index in indices]
        merged = ' '.join(lines_to_merge)

        indices.reverse()
        for index in indices:
            del self.lines[index]

        self.lines.insert(first_index, merged)
        return self

    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        if self.lines[index] == '':
            self.lines[index] = punctuation
        elif self.lines[index][-1] in EOL_PUNCTUATION:
            self.lines[index] = self.lines[index][:-1]
            self.lines[index] += punctuation
        else:
            self.lines[index] += punctuation
        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        lines = [self._remove_punctuation(line) for line in self.lines]
        words = ' '.join(lines).split()
        return len(words)

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        lines = [self._remove_punctuation(line) for line in self.lines]
        words = ' '.join(lines).split()
        words = sorted(set([word.lower() for word in words]))
        return words

    @staticmethod
    def _remove_punctuation(line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        for char in EOL_PUNCTUATION:
            line = line.replace(char, '')
        return line

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        return '\n'.join(self.lines)


if __name__ == "__main__":
    # this part is only execute when you run the file and
    # is ignored by the tests
    # you can use this section for debugging and testing
    d = (
        Document()
        .add_line("My first sentence.")
        .add_line("My second sentence.")
        .add_line("Introduction", 0)
        .merge_lines([1, 2])
    )

    print(d)
    print(len(d))
    print(d.word_count())
    print(d.words)
