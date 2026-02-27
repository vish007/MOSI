from shared.event_store import append_event, replay


def test_append_and_replay():
    append_event('test-stream', 'created', {'id': 1})
    events = replay('test-stream')
    assert events
    assert events[-1]['event_type'] == 'created'
