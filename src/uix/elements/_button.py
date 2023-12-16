from ..core.element import Element
print("Imported: Button")
class button(Element):
    def __init__(self,value,id = None, type='button', formID=None, disabled=False):
        super().__init__(value, id = id)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.classes.append("btn")
        self.disabled = disabled

        if formID is not None:
            self.attrs["form"] = formID

        if self.disabled:
            self.attrs["disabled"] = "disabled"

    def bind(self,session):
        if self.id is None:
            self.id = "btn_" + str(session.next_id())
        super().bind(session)
        