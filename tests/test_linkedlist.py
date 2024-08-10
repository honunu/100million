from storage.linked_list import LinkedList


def test_add():
    list = LinkedList()

    for i in range(10):
        list.add(i)

    assert list.get(8) is not None


def test_remove():
    list = LinkedList()

    for i in range(10):
        list.add(i)

    list.remove(8)

    assert list.get(8) is None
