import unittest
from unittest.mock import patch
import io
import xml.etree.ElementTree
from Elena_Vikenteva_lab_NYSE_xml import main


class TestMain(unittest.TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_output(self, mock_stdout):
        xml_data = """
            <quotes>
                <quote last="100" change="+10" min="90" max="110">Company1</quote>
                <quote last="50" change="-5" min="45" max="55">Company2</quote>
            </quotes>
        """
        with patch("builtins.open", new=io.StringIO(xml_data)) as mock_open:
            with patch(
                "xml.etree.ElementTree.parse", side_effect=xml.etree.ElementTree.parse
            ) as mock_parse:
                main()

                expected_output = (
                    "COMPANY                              LAST      CHANGE    MIN       MAX       \n"
                    "--------------------------------------------------------------------------------\n"
                    "Company1                             100       +10       90        110       \n"
                    "Company2                             50        -5        45        55        \n"
                )

                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_main_file_not_found(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            with patch("builtins.open", side_effect=FileNotFoundError):
                main()
                self.assertIn("Stock data file not found", mock_stdout.getvalue())

    def test_main_invalid_data(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            with patch(
                "xml.etree.ElementTree.parse",
                side_effect=xml.etree.ElementTree.ParseError,
            ):
                main()
                self.assertIn(
                    "Stock data file contains invalid data", mock_stdout.getvalue()
                )


if __name__ == "__main__":
    unittest.main()
