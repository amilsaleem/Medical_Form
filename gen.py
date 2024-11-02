
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
import math

form_data = {
    1: {
        "SlNo": "001",
        "BillNo": "2407680 15-07-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Consultation",
        "Amount": "1000",
        "Remarks": ""
    },
    2: {
        "SlNo": "001",
        "BillNo": "23073014 10-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Discharge",
        "Amount": "433407",
        "Remarks": ""
    },
    3: {
        "SlNo": "001",
        "BillNo": "470486693 15-08-24",
        "SupplierName": "lal Path Labs",
        "Particulars": "Test",
        "Amount": "876",
        "Remarks": ""
    },
    4: {
        "SlNo": "001",
        "BillNo": "240826497 16-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Consultation",
        "Amount": "1000",
        "Remarks": ""
    },
    5: {
        "SlNo": "001",
        "BillNo": "95 16-08-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "2520",
        "Remarks": ""
    }, 
    6:{
        "SlNo": "001",
        "BillNo": "22230310210034 21-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Medicine",
        "Amount": "372",
        "Remarks": ""
    },
    7: {
        "SlNo": "001",
        "BillNo": "180277123 21-08-24",
        "SupplierName": "lal Path Labs",
        "Particulars": "Test",
        "Amount": "333",
        "Remarks": ""
    },
    8: {
        "SlNo": "001",
        "BillNo": "240837366 21-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Consultation",
        "Amount": "1000",
        "Remarks": ""
    },

    9: {
        "SlNo": "001",
        "BillNo": "106 22-08-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "5305",
        "Remarks": "Need Correction"
    },
    10: {
        "SlNo": "001",
        "BillNo": "240838830 23-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Consultation",
        "Amount": "1000",
        "Remarks": ""
    },
    11: {
        "SlNo": "001",
        "BillNo": "240838783 23-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Test",
        "Amount": "1240",
        "Remarks": ""
    },
    12: {
        "SlNo": "001",
        "BillNo": "240839111 23-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Test",
        "Amount": "1415",
        "Remarks": ""
    },
    13: {
        "SlNo": "001",
        "BillNo": "22230280076401 23-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Treatment",
        "Amount": "903",
        "Remarks": ""
    },
    14: {
        "SlNo": "001",
        "BillNo": "108 23-08-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "500",
        "Remarks": "Verify"
    },
    15: {
        "SlNo": "001",
        "BillNo": "120124OPCS190320 28-08-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Test",
        "Amount": "800",
        "Remarks": ""
    },
    16: {
        "SlNo": "001",
        "BillNo": "120124OPCS191268 29-08-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Tests",
        "Amount": "270",
        "Remarks": ""
    },
    17: {
        "SlNo": "001",
        "BillNo": "22230310213808 29-08-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Medicine",
        "Amount": "233",
        "Remarks": ""
    },
    18: {
        "SlNo": "001",
        "BillNo": "120124OPCS193446 31-08-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Consultation",
        "Amount": "350",
        "Remarks": ""
    },
    19: {
        "SlNo": "001",
        "BillNo": "CREATE 31-08-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "0",
        "Remarks": "Create"
    },
    20: {
        "SlNo": "001",
        "BillNo": "240860374 03-09-24",
        "SupplierName": "Holy Family Hospital",
        "Particulars": "Consultation",
        "Amount": "1000",
        "Remarks": ""
    },
    21: {
        "SlNo": "001",
        "BillNo": "113 03-09-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "9177",
        "Remarks": "Correction"
    },
    22: {
        "SlNo": "001",
        "BillNo": "Create 19-09-24",
        "SupplierName": "Insha Pharmacy",
        "Particulars": "Medicine",
        "Amount": "0",
        "Remarks": "Create"
    },
    23: {
        "SlNo": "001",
        "BillNo": "120124OPCS211057 20-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Consultation",
        "Amount": "350",
        "Remarks": ""
    },
    24: {
        "SlNo": "001",
        "BillNo": "120124OPCS212632 21-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    25: {
        "SlNo": "001",
        "BillNo": "120124OPCS213715 23-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    26: {
        "SlNo": "001",
        "BillNo": "120124OPCS214860 24-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    27: {
        "SlNo": "001",
        "BillNo": "120124OPCS215819 25-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    28: {
        "SlNo": "001",
        "BillNo": "120124OPCS216911 26-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    29: {
        "SlNo": "001",
        "BillNo": "120124OPCS216843 26-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Consultation",
        "Amount": "350",
        "Remarks": ""
    },
    30: {
        "SlNo": "001",
        "BillNo": "120124OPCS218955 28-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    31: {
        "SlNo": "001",
        "BillNo": "120124OPCS219978 30-09-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    32: {
        "SlNo": "001",
        "BillNo": "120124OPCS221048 01-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    33: {
        "SlNo": "001",
        "BillNo": "120124OPCS222212 03-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    34: {
        "SlNo": "001",
        "BillNo": "120124OPCS224353 05-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    35: {
        "SlNo": "001",
        "BillNo": "120124OPCS225540 07-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    36: {
        "SlNo": "001",
        "BillNo": "120124OPCS226731 08-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    37: {
        "SlNo": "001",
        "BillNo": "120124OPCS227774 09-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    38: {
        "SlNo": "001",
        "BillNo": "120124OPCS228744 10-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    39: {
        "SlNo": "001",
        "BillNo": "120124OPCS231023 14-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    40: {
        "SlNo": "001",
        "BillNo": "120124OPCS233329 16-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    41: {
        "SlNo": "001",
        "BillNo": "120124OPCS235230 18-10-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Dressing",
        "Amount": "300",
        "Remarks": ""
    },
    

    42: {
        "SlNo": "001",
        "BillNo": "120124OPCS191268 29-08-24",
        "SupplierName": "Fortis Escorts Hospital",
        "Particulars": "Tests",
        "Amount": "270",
        "Remarks": ""
    }
    


    
    
    
    
    

    

 }

# Function to create an overlay PDF with form data
def create_overlay(data, count=0,amount=None):
    packet = BytesIO()
    can = canvas.Canvas(packet)
    y = 724

    for entry in data.values():
        count += 1
        can.drawString(15, y, str(count))
        if len(entry["BillNo"])>18:
            can.setFont("Helvetica", 9)  
            if len(entry["BillNo"])>24:
                can.setFont("Helvetica", 8)

        can.drawString(40, y, entry["BillNo"])
        can.setFont("Helvetica", 10)
        can.drawString(160, y, entry["SupplierName"])
        can.drawString(300, y, entry["Particulars"])
        can.drawString(430, y, entry["Amount"])
        can.drawString(550, y, entry["Remarks"])
        y -= 25.5
    if amount:
        can.setFont("Helvetica-Bold", 14)
        can.drawString(300, y, "Total")
        can.drawString(430, y,str(amount))
    
    can.save()
    packet.seek(0)
    return packet

# Paths to the input and output PDF files
input_pdf_path = 'form.pdf'
output_pdf_path = 'filled_form.pdf'

# Load the original PDF and initialize the writer
original_pdf = PdfReader(input_pdf_path)
output_pdf = PdfWriter()

# Define batch size and initialize counters
batch_size = 28
total_entries = len(form_data)

# Process data in batches
for i in range(0, total_entries, batch_size):


    total_amount = sum(int(entry["Amount"]) for entry in form_data.values())

    # Slice the form data dictionary for the current batch
    batch_data = {k: form_data[k] for k in list(form_data.keys())[i:i + batch_size]}

    if (i+batch_size>total_entries): 
        overlay_pdf = PdfReader(create_overlay(batch_data, count=i,amount=total_amount))
    else:
        overlay_pdf = PdfReader(create_overlay(batch_data, count=i))
    # Reload the original page each time to ensure a fresh page
    page = PdfReader(input_pdf_path).pages[0]
    page.merge_page(overlay_pdf.pages[0])  # Merge overlay onto this fresh page

    # Add the merged page to the output PDF
    output_pdf.add_page(page)

print(output_pdf.pages)
# Write to a new PDF file
with open(output_pdf_path, "wb") as output_file:
    output_pdf.write(output_file)

print("Inserted Data:")
