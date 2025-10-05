from app.history import History

def test_add_observer_and_callback():
    h = History()
    called = {"flag": False}

    class DummyObserver:
        def on_calculation(self, calc, result):
            called["flag"] = True

    h.add_observer(DummyObserver())

    # Fake minimal "calc" with needed attributes
    class FakeOp: ...
    class FakeCalc:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.op = FakeOp()

    h.record(FakeCalc(), 3)
    assert called["flag"] is True
