from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from erpnext_thailand.constants import ERP_CUSTOM_FIELDS

def execute():
    custom_fields = {
        "Thai Tax Settings Company": list(filter(lambda l: l["fieldname"] in ["purchase_tax_account_non_recoverable"], ERP_CUSTOM_FIELDS["Thai Tax Settings Company"]))
    }
    create_custom_fields(custom_fields, ignore_validate=True)
