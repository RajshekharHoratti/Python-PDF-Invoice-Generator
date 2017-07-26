import datetime
import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



# createpdf function to create a pdf file
def cratepdf(companynamepdf, companyaddresspdf, amountpdf, staxpdf, emailpdf, timestamppdf, canvas2, datepdf, finalstaxpdf, productpdf):
    canvas = canvas2.Canvas("/home/raj/Documents/MyProjects/Python Invoice Pdf Generator/INVOICE/Invoice (" + str(timestamppdf) + ").pdf", pagesize=letter)

    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)

    canvas.line(50, 747, 580, 747) #FROM TOP 1ST LINE
    canvas.drawString(280, 750, "INVOICE")
    canvas.drawString(60, 720, "COMPANY NAME:- "+ companynamepdf)
    canvas.drawString(60, 690, "EMAIL-ID:- "+ emailpdf)
    canvas.drawString(60, 660, "ADDRESS:- "+ companyaddresspdf)
    canvas.drawString(450, 720, "DATE :- "+ str(datepdf))
    canvas.line(450, 710, 560, 710)
    canvas.line(50, 640, 580, 640)#FROM TOP 2ST LINE
    canvas.line(50, 748, 50, 50)#LEFT LINE
    canvas.line(400, 640, 400, 50)# MIDDLE LINE
    canvas.line(580, 748, 580, 50)# RIGHT LINE
    canvas.drawString(475, 615, 'TOTAL AMOUNT')
    canvas.drawString(100, 615, 'PRODUCT')
    canvas.line(50, 600, 580, 600)#FROM TOP 3rd LINE
    canvas.drawString(60, 550, productpdf)
    canvas.drawString(500, 550, amountpdf)
    TOTAL = int(amountpdf) * ((int(staxpdf)) / 100)
    canvas.drawString(60, 500, "SERVICE TAX (" +staxpdf+"%)")
    canvas.drawString(500, 500, str(TOTAL))
    canvas.line(50, 100, 580, 100)#FROM TOP 4th LINE
    canvas.drawString(60, 80, " TOTAL AMOUNT")
    canvas.drawString(500, 80, str(finalstaxpdf))
    canvas.line(50, 50, 580, 50)#FROM TOP LAST LINE
    canvas.save()
#
#

companyname = "YOUR COMPANY NAME"
companyaddress = "COMPANY ADDRESS"
amount = "10000"
stax = "18"
email = "TEST@TEST.COM"
product = "Office Table"
timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
date = time.strftime("%d/%m/%Y")
finalstax = int(amount) + (int(amount) * ((int(stax))/100))
cratepdf(companyname, companyaddress, amount, stax, email, timestamp, canvas, date, finalstax, product)