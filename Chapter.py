import re


class Chapter:
    def __init__(self, title: str, content: str) -> None:
        self.title = title.text
        self.content = content

    def get_sanitized_title(self):
        title_string = self.title
        debug_me = re.sub(r"(?u)[^-\w.]", "", title_string)
        return debug_me

    def __str__(self):
        return f"{self.title}\n {self.content}"
