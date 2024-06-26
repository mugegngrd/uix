from ..core.element import Element
print("Imported: grid")
class grid(Element):
    def __init__(self,value:str = None, id:str = None, columns:str = None, rows:str = None):
        super().__init__(value, id = id)
        self.style("display", "grid")
        if columns is not None:
            self.style("grid-template-columns", columns)
        else:
            self.style("grid-template-columns", "auto auto")
        if rows is not None:
            self.style("grid-template-rows", rows)
        else:
            self.style("grid-template-rows", "auto auto")

