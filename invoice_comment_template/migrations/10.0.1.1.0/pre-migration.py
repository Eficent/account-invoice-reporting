# -*- coding: utf-8 -*-
# Copyright 2018 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

_column_renames = {
    'account_invoice': [
        ('text_condition1', None),
        ('text_condition2', None),
    ],
}


@openupgrade.migrate(use_env=False)
def migrate(cr, version):
    openupgrade.rename_columns(cr, _column_renames)
