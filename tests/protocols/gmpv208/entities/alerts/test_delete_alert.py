# SPDX-FileCopyrightText: 2018-2024 Greenbone AG
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gvm.errors import RequiredArgument


class GmpDeleteAlertTestMixin:
    def test_delete(self):
        self.gmp.delete_alert("a1")

        self.connection.send.has_been_called_with(
            b'<delete_alert alert_id="a1" ultimate="0"/>'
        )

    def test_delete_ultimate(self):
        self.gmp.delete_alert("a1", ultimate=True)

        self.connection.send.has_been_called_with(
            b'<delete_alert alert_id="a1" ultimate="1"/>'
        )

    def test_missing_alert_id(self):
        with self.assertRaises(RequiredArgument):
            self.gmp.delete_alert(None)

        with self.assertRaises(RequiredArgument):
            self.gmp.delete_alert("")
