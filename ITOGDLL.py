import ctypes
import os

# Загружаем DLL (файл должен лежать рядом)
_dll_path = os.path.abspath('./spisok_dll.dll')
_dll = ctypes.CDLL(_dll_path)

# Настраиваем типы функций DLL
_dll.dobavit_v_nachalo.argtypes = [ctypes.c_int]
_dll.dobavit_v_nachalo.restype = None

_dll.dobavit_v_konec.argtypes = [ctypes.c_int]
_dll.dobavit_v_konec.restype = None

_dll.udalit_s_nachala.argtypes = []
_dll.udalit_s_nachala.restype = ctypes.c_int

_dll.udalit_s_konca.argtypes = []
_dll.udalit_s_konca.restype = ctypes.c_int

_dll.uznat_razmer.argtypes = []
_dll.uznat_razmer.restype = ctypes.c_int

_dll.naiti_po_pozicii.argtypes = [ctypes.c_int]
_dll.naiti_po_pozicii.restype = ctypes.c_int

_dll.udalit_po_pozicii.argtypes = [ctypes.c_int]
_dll.udalit_po_pozicii.restype = ctypes.c_int

_dll.ochistit_spisok.argtypes = []
_dll.ochistit_spisok.restype = None

_dll.proverit_na_pustotu.argtypes = []
_dll.proverit_na_pustotu.restype = ctypes.c_bool


# =========================================================
# КЛАСС-АДАПТЕР (тот же интерфейс, что и в Python-версии)
# =========================================================
class SraniyCiklicheskiyDvusvyazniySpisok:
    """
    Обёртка над C++ DLL.
    Все методы имеют те же имена и возвращают те же типы,
    что и в чистой Python-реализации.
    """

    def __init__(self):
        # В DLL список глобальный, но для совместимости
        # вызываем очистку при создании нового объекта
        _dll.ochistit_spisok()

    def dobavit_v_nachalo(self, data):
        # Конвертируем строку в число (DLL работает только с int)
        try:
            value = int(data)
        except (ValueError, TypeError):
            return  # Игнорируем нечисловые данные, как в оригинале
        _dll.dobavit_v_nachalo(value)

    def dobavit_v_konec(self, data):
        try:
            value = int(data)
        except (ValueError, TypeError):
            return
        _dll.dobavit_v_konec(value)

    def naiti_po_pozicii(self, position):
        result = _dll.naiti_po_pozicii(int(position))
        # DLL возвращает -999 при ошибке → конвертируем в None
        return result if result != -999 else None

    def udalit_po_pozicii(self, position):
        result = _dll.udalit_po_pozicii(int(position))
        return result if result != -999 else None

    def display(self):
        """Возвращает список строк, как в Python-версии"""
        size = _dll.uznat_razmer()
        if size == 0:
            return []
        elements = []
        for i in range(size):
            val = _dll.naiti_po_pozicii(i)
            elements.append(str(val))  # Конвертируем int → str
        return elements

    # Дополнительные методы (если вдруг интерфейс их использует)
    def pusto(self):
        return _dll.proverit_na_pustotu()

    def udalit_s_nachala(self):
        result = _dll.udalit_s_nachala()
        return result if result != -1 else None

    def udalit_s_konca(self):
        result = _dll.udalit_s_konca()
        return result if result != -1 else None