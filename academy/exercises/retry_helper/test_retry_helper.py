import unittest

from retry_helper import retry


class RetryTests(unittest.TestCase):
    def test_returns_first_success(self):
        calls = []

        def operation():
            calls.append(1)
            return "ok"

        self.assertEqual(retry(operation, 3), "ok")
        self.assertEqual(len(calls), 1)

    def test_retries_until_success(self):
        attempts = {"count": 0}

        def operation():
            attempts["count"] += 1
            if attempts["count"] < 3:
                raise RuntimeError("temporary")
            return "done"

        self.assertEqual(retry(operation, 3), "done")
        self.assertEqual(attempts["count"], 3)

    def test_reraises_final_exception(self):
        attempts = {"count": 0}

        def operation():
            attempts["count"] += 1
            raise ValueError(f"failure {attempts['count']}")

        with self.assertRaisesRegex(ValueError, "failure 3"):
            retry(operation, 3)
        self.assertEqual(attempts["count"], 3)

    def test_one_attempt_means_one_call(self):
        calls = []

        def operation():
            calls.append(1)
            return 42

        self.assertEqual(retry(operation, 1), 42)
        self.assertEqual(len(calls), 1)


if __name__ == "__main__":
    unittest.main()
