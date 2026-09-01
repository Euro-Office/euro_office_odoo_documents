from odoo import fields, models


class EuroOfficeDocumentsAccessUser(models.Model):
    _name = "euro_office.odoo.documents.access"
    _description = "Euro-Office Documents Access"

    document_id = fields.Many2one("documents.document", required=True, ondelete="cascade")
    internal_users = fields.Selection(
        [
            ("none", "None"),
            ("view", "Viewer"),
            ("commenter", "Commenter"),
            ("reviewer", "Reviewer"),
            ("edit", "Editor"),
            ("form_filling", "Form Filling"),
            ("custom_filter", "Custom Filter"),
        ],
        default="none",
        string="Internal Users Access",
    )
    link_access = fields.Selection(
        [
            ("none", "None"),
            ("view", "Viewer"),
            ("commenter", "Commenter"),
            ("reviewer", "Reviewer"),
            ("edit", "Editor"),
            ("form_filling", "Form Filling"),
            ("custom_filter", "Custom Filter"),
        ],
        default="view",
        string="Link Access",
    )
