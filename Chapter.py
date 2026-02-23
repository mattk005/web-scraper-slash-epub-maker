class Chapter:
    def __init__(self, title: str, paragraphs: list[str | list]) -> None:
        self.title = title
        self.paragraphs = paragraphs

    def __str__(self):
        return f"{self.title}\n {self.paragraphs}"
