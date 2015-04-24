# -*- coding: utf-8 -*-
# (c) 2015 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
import os
from unittest.case import TestCase
from bright_fabric.util import find_files


class UtilTests(TestCase):

    test_data_path = os.path.join(os.path.dirname(__file__), 'test_data')
    txt_in_path = [
        'one.txt',
        'two.txt',
    ]

    dat_in_path = [
        'one.dat'
    ]

    txt_in_subdir = [
        os.path.join('subdir', 'three.txt')
    ]

    def test_find_files_finds_expected_in_folder_when_using_suffix(self):
        files = find_files(self.test_data_path, ['txt'])
        self.assertFilesReturned(files, self.txt_in_path + self.txt_in_subdir)

    def test_can_exclude_folders_from_find_files(self):
        files = find_files(self.test_data_path, ['txt'], exclude_dirs=['subdir'])
        self.assertFilesReturned(files, self.txt_in_path)

    def test_can_add_multiple_extensions_in_filter(self):
        files = find_files(self.test_data_path, ['txt', 'dat'], exclude_dirs=['subdir'])
        self.assertFilesReturned(files, self.txt_in_path + self.dat_in_path)

    def test_running_without_setting_suffixes_returns_all_suffixes(self):
        files = find_files(self.test_data_path, exclude_dirs=['subdir'])
        self.assertFilesReturned(files, self.txt_in_path + self.dat_in_path)


    def assertFilesReturned(self, files, expected_files):
        self.assertEqual(len(expected_files), len(files))
        for file_path in [os.path.join(self.test_data_path, file_name) for
                          file_name in self.txt_in_path]:
            self.assertIn(file_path, files)
