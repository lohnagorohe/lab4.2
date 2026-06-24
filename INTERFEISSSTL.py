import spisok_pybind

class SraniyCiklicheskiyDvusvyazniySpisok:
    def __init__(self):
        self.spisok = spisok_pybind.Spisok()

    def dobavit_v_nachalo(self, data):
        try:
            self.spisok.push_front(int(data))
        except (ValueError, TypeError):
            pass

    def dobavit_v_konec(self, data):
        try:
            self.spisok.push_back(int(data))
        except (ValueError, TypeError):
            pass

    def udalit_s_nachala(self):
        if self.spisok.empty():
            return None
        value = self.spisok.front()
        self.spisok.pop_front()
        return value

    def udalit_s_konca(self):
        if self.spisok.empty():
            return None
        value = self.spisok.back()
        self.spisok.pop_back()
        return value

    def naiti_po_pozicii(self, position):
        try:
            return self.spisok.get_at(position)
        except:
            return None

    def udalit_po_pozicii(self, position):
        try:
            return self.spisok.remove_at(position)
        except:
            return None

    def display(self):
        elements = self.spisok.to_vector()
        return [str(e) for e in elements]

    def pusto(self):
        return self.spisok.empty()