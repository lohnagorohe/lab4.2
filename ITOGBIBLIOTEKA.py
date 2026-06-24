class uzel:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SraniyCiklicheskiyDvusvyazniySpisok:
    def __init__(self):
        self.golova = None

    def pusto(self):
        return self.golova is None

    def dobavit_v_nachalo(self, data):
        new_uzel = uzel(data)
        if self.pusto():
            new_uzel.next = new_uzel
            new_uzel.prev = new_uzel
            self.golova = new_uzel
        else:
            hvost = self.golova.prev
            new_uzel.next = self.golova
            new_uzel.prev = hvost
            self.golova.prev = new_uzel
            hvost.next = new_uzel
            self.golova = new_uzel

    def dobavit_v_konec(self, data):
        new_uzel = uzel(data)
        if self.pusto():
            new_uzel.next = new_uzel
            new_uzel.prev = new_uzel
            self.golova = new_uzel
        else:
            hvost = self.golova.prev
            new_uzel.next = self.golova
            new_uzel.prev = hvost
            hvost.next = new_uzel
            self.golova.prev = new_uzel

    def udalit_s_nachala(self):
        if self.pusto():
            return None
        if self.golova.next == self.golova:
            data = self.golova.data
            self.golova = None
            return data
        else:
            hvost = self.golova.prev
            data = self.golova.data
            self.golova = self.golova.next
            self.golova.prev = hvost
            hvost.next = self.golova
            return data

    def udalit_s_konca(self):
        if self.pusto():
            return None
        if self.golova.next == self.golova:
            data = self.golova.data
            self.golova = None
            return data
        else:
            hvost = self.golova.prev
            data = hvost.data
            new_hvost = hvost.prev
            new_hvost.next = self.golova
            self.golova.prev = new_hvost
            return data

    def naiti_po_pozicii(self, position):
        if self.pusto() or position < 0:
            return None
        sechas = self.golova
        schetchik = 0
        while schetchik < position:
            sechas = sechas.next
            schetchik += 1
            if sechas == self.golova:
                return None
        return sechas.data

    def udalit_po_pozicii(self, position):
        if self.pusto() or position < 0:
            return None
        if self.golova.next == self.golova and position == 0:
            data = self.golova.data
            self.golova = None
            return data
        sechas = self.golova
        schetchik = 0
        while schetchik < position:
            sechas = sechas.next
            schetchik += 1
            if sechas == self.golova:
                return None
        data = sechas.data
        sechas.prev.next = sechas.next
        sechas.next.prev = sechas.prev
        if sechas == self.golova:
            self.golova = sechas.next
        return data

    def display(self):
        if self.pusto():
            return []
        elements = []
        sechas = self.golova
        while True:
            elements.append(str(sechas.data))
            sechas = sechas.next
            if sechas == self.golova:
                break
        return elements