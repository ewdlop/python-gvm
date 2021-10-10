# -*- coding: utf-8 -*-
# Copyright (C) 2018-2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Latest supported stable protocols.

This module exposes the latest supported protocols for the newest stable
release branch of GVM.

The provided Gmp class implements the latest `Greenbone Management
Protocol`_.
The provided Osp class implements the latest Open Scanner Protocol.

For details about the possible supported protocol versions please take a look at
:py:mod:`gvm.protocols`.

Exports:
  - :py:class:`gvm.protocols.gmpv208.Gmp`
  - :py:class:`gvm.protocols.ospv1.Osp`

.. _Greenbone Management Protocol:
    https://docs.greenbone.net/API/GMP/gmp.html
"""

from .gmpv208 import (
    Gmp,
    AggregateStatistic,
    AlertCondition,
    AlertEvent,
    AlertMethod,
    AliveTest,
    CredentialFormat,
    CredentialType,
    EntityType,
    FeedType,
    FilterType,
    HelpFormat,
    HostsOrdering,
    InfoType,
    PermissionSubjectType,
    PortRangeType,
    ReportFormatType,
    ScannerType,
    SeverityLevel,
    SnmpAuthAlgorithm,
    SnmpPrivacyAlgorithm,
    SortOrder,
    TicketStatus,
    UserAuthType,
)
from .ospv1 import Osp

__all__ = [
    "Gmp",
    "Osp",
    "AggregateStatistic",
    "AlertCondition",
    "AlertEvent",
    "AlertMethod",
    "AliveTest",
    "CredentialType",
    "CredentialFormat",
    "EntityType",
    "FeedType",
    "FilterType",
    "HelpFormat",
    "HostsOrdering",
    "InfoType",
    "PermissionSubjectType",
    "PortRangeType",
    "ReportFormatType",
    "ScannerType",
    "SeverityLevel",
    "SnmpAuthAlgorithm",
    "SnmpPrivacyAlgorithm",
    "SortOrder",
    "TicketStatus",
    "UserAuthType",
]
