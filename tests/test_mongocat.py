#!/usr/bin/env python

"""Tests for `mongocat` package."""


import unittest
from click.testing import CliRunner

from mongocat import cli


class TestMongocat(unittest.TestCase):
    """Tests for `mongocat` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        help_result = runner.invoke(cli.cli, ['--help'])
        assert help_result.exit_code == 0
        assert 'Usage:' in help_result.output
