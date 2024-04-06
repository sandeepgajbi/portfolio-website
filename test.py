import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import streamlit as st
import main


class TestMain(unittest.TestCase):
    @patch('streamlit.image')
    @patch('streamlit.title')
    @patch('streamlit.info')
    def test_display_portfolio_header(self, mock_info, mock_title, mock_image):

        # Call the function
        main.display_portfolio_header(st)

        # Assertions
        mock_image.assert_called_once_with(main.PHOTO_PATH, use_column_width="auto", output_format="auto")
        mock_title.assert_called_once_with(main.NAME)
        mock_info.assert_called_once_with(main.intro.CONTENT)

    @patch('pandas.read_csv')
    def test_read_csv_file(self, mock_read_csv):
        # Mock data
        mock_read_csv.return_value = pd.DataFrame({'title': ['App 1'], 'description': ['Description 1'],
                                                   'image': ['app1.png'], 'url': ['http://example.com/app1']})

        # Call the function
        df = main.read_csv_file("test.csv", pd)

        # Assertions
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['title'], 'App 1')

    @patch('streamlit.image')
    @patch('streamlit.write')
    def test_display_app_details(self, mock_write, mock_image):
        # Mock data
        df = pd.DataFrame({
            'title': ['App 1', 'App 2'],
            'description': ['Description 1', 'Description 2'],
            'image': ['app1.png', 'app2.png'],
            'url': ['http://example.com/app1', 'http://example.com/app2']
        })

        col_mock = MagicMock()
        start_index = 0
        end_index = 1

        # Call the function
        main.display_app_details(st, col_mock, df, start_index, end_index)

        # Assertions
        mock_image.assert_called_once_with("images/app1.png")
        mock_write.assert_any_call("[Source Code](http://example.com/app1)")


if __name__ == '__main__':
    unittest.main()