import io
import unittest
from contextlib import redirect_stdout

import main


class MainTests(unittest.TestCase):
    def test_main_prints_running_message(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main.main()

        self.assertEqual(buffer.getvalue().strip(), "Emergent app builder is running.")


if __name__ == "__main__":
    unittest.main()
