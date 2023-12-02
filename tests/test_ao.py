CANT_FIND_PREFIX = "Can't find a wikipedia entry for "


def test_sanity():
    from ao import apple
    assert CANT_FIND_PREFIX not in apple


def test_sanity_import_without_from():
    import ao
    assert CANT_FIND_PREFIX not in ao.apple


def test_from_ao_import_ao():
    from ao import ao
    assert CANT_FIND_PREFIX not in ao


def test_number():
    from ao import _1999
    assert CANT_FIND_PREFIX not in _1999


def test_no_entry():
    from ao import gggg
    assert CANT_FIND_PREFIX in gggg


def test_multiple_requests():
    import ao
    for _ in range(20):
        assert CANT_FIND_PREFIX not in ao.apple


def test_just_import_ao():
    import ao
    assert "module 'ao'" in str(ao)
