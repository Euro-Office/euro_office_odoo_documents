from odoo import fields, models


class EuroOfficeDocumentsAccessUser(models.Model):
    _name = "euro_office.odoo.documents.access.user"
    _description = "Euro-Office Documents Access Users"

    document_id = fields.Many2one("documents.document", required=True, ondelete="cascade")
    user_id = fields.Many2one("res.partner", required=True, string="User")
    role = fields.Selection(
        [
            ("none", "None"),
            ("view", "Viewer"),
            ("commenter", "Commenter"),
            ("reviewer", "Reviewer"),
            ("edit", "Editor"),
            ("form_filling", "Form Filling"),
            ("custom_filter", "Custom Filter"),
        ],
        required=True,
        string="Access Level",
    )
