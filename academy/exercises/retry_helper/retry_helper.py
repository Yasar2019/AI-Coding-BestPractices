def retry(operation, max_attempts):
    """Call operation until it succeeds or attempts are exhausted."""
    last_error = None

    # Intentionally buggy starter implementation for Lab 03.
    for _ in range(max_attempts - 1):
        try:
            result = operation()
        except Exception as exc:
            last_error = exc
            continue

    if last_error is not None:
        return None

    return result
