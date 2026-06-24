#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <list>
#include <vector>

namespace py = pybind11;

class CyclicList {
private:
    std::list<int> data;

public:
    void push_front(int value) {
        data.push_front(value);
    }

    void push_back(int value) {
        data.push_back(value);
    }

    void pop_front() {
        if (!data.empty()) {
            data.pop_front();
        }
    }

    void pop_back() {
        if (!data.empty()) {
            data.pop_back();
        }
    }

    int front() {
        if (data.empty()) throw std::runtime_error("Список пуст");
        return data.front();
    }

    int back() {
        if (data.empty()) throw std::runtime_error("Список пуст");
        return data.back();
    }

    bool empty() {
        return data.empty();
    }

    size_t size() {
        return data.size();
    }

    void clear() {
        data.clear();
    }

    int get_at(int position) {
        if (position < 0 || position >= (int)data.size())
            throw std::out_of_range("Позиция вне диапазона");
        auto it = data.begin();
        std::advance(it, position);
        return *it;
    }

    int remove_at(int position) {
        if (position < 0 || position >= (int)data.size())
            throw std::out_of_range("Позиция вне диапазона");
        auto it = data.begin();
        std::advance(it, position);
        int value = *it;
        data.erase(it);
        return value;
    }

    std::vector<int> to_vector() {
        return std::vector<int>(data.begin(), data.end());
    }
};

PYBIND11_MODULE(spisok_pybind, m) {
    m.doc() = "Модуль списка на C++ с STL";

    py::class_<CyclicList>(m, "Spisok")
        .def(py::init<>())
        .def("push_front", &CyclicList::push_front)
        .def("push_back", &CyclicList::push_back)
        .def("pop_front", &CyclicList::pop_front)
        .def("pop_back", &CyclicList::pop_back)
        .def("front", &CyclicList::front)
        .def("back", &CyclicList::back)
        .def("empty", &CyclicList::empty)
        .def("size", &CyclicList::size)
        .def("clear", &CyclicList::clear)
        .def("__len__", &CyclicList::size)
        .def("to_vector", &CyclicList::to_vector)
        .def("get_at", &CyclicList::get_at)
        .def("remove_at", &CyclicList::remove_at);
}