# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Wallet Sale",
    "summary": """
        Allows to manage wallet on sale level""",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "Odoo Community Association (OCA), ACSONE SA/NV",
    "website": "https://github.com/OCA/wallet",
    "depends": [
        "sale",
        "account_wallet",
    ],
    "external_dependencies": {"python": ["openupgradelib"]},
    "data": [
        "security/security.xml",
        "views/account_wallet.xml",
        "views/sale_order.xml",
        "wizards/sale_wallet_pay.xml",
    ],
}
