# -*- coding: utf-8 -*-
# (c) 2015 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from unittest.case import TestCase
from fabric.state import env
from mock import MagicMock, patch
from bright_fabric.tasks import pylint
from tests.util import ArgumentCaptor, OverrideFabricConfig


class TaskTests(TestCase):

    def setUp(self):
        self.mock_fabric_api = MagicMock()

    @patch('bright_fabric.tasks.local')
    def test_pylint_runs_without_ignores_by_default(self, mock_local):
        pylint()
        captor = ArgumentCaptor()
        mock_local.assert_called_with(captor)
        self.assertTrue(all([
            captor.argument.startswith('flake8'),
            '--ignore' not in captor.argument,
        ]))

    @patch('bright_fabric.tasks.local')
    def test_pylint_runs_flake_with_ignores_if_configured(self, mock_local):
        with OverrideFabricConfig(flake8_ignores=['E591', 'E100']):
            pylint()
            captor = ArgumentCaptor()
            mock_local.assert_called_with(captor)
            self.assertTrue(all([
                captor.argument.startswith('flake8'),
                '--ignore=E591,E100' in captor.argument,
            ]))
