class PrinterError(RuntimeError):
    pass


class Printer:
    def __init__(self, capacity: int):
        self.capacity = capacity

    @property
    def remaining_pages(self):
        return self.capacity

    def print(self, pages):
        if self.capacity < pages:
            raise PrinterError
        self.capacity -= pages
        return f"printed {pages} pages."


printer = Printer(300)
print(printer.print(25))
print(f"Páginas restantes {printer.remaining_pages}")

