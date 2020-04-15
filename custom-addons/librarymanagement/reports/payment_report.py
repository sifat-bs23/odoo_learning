from odoo import models


class PaymentXlsx(models.AbstractModel):
    _name = 'report.librarymanagement.payment_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, payments):

        format1 = workbook.add_format({'font_size': 10, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet("Test Report")
        sheet.write(0, 0, "Rental ID", format1)
        sheet.write(0, 1, "Customer Name", format1)
        sheet.write(0, 2, "Customer Phone", format1)
        sheet.write(0, 3, "Customer Mail", format1)
        sheet.write(0, 4, "Due Amount", format1)
        sheet.write(0, 5, "Extra Amount", format1)
        sheet.write(0, 6, "Total Amount", format1)
        row = 1
        for payment in payments:
            sheet.write(row, 0, payment.rental_ids[0].id if payment.rental_ids[0].id else 'N/A', format2)
            sheet.write(row, 1, payment.customer_ids.first_name if payment.customer_ids.first_name else 'N/A', format2)
            sheet.write(row, 2, payment.customer_ids.phone if payment.customer_ids.phone else 'N/A', format2)
            sheet.write(row, 3, payment.customer_ids.email if payment.customer_ids.email else 'N/A', format2)
            sheet.write(row, 4, payment.due_amount if payment.due_amount else '0.00', format2)
            sheet.write(row, 5, payment.extra_charge if payment.extra_charge else '0.00', format2)
            sheet.write(row, 6, payment.total_amount if payment.total_amount else '0.00', format2)
            row += 1
