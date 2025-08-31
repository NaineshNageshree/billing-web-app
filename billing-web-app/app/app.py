from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        product = request.form.get("product")
        quantity = int(request.form.get("quantity"))
        price = float(request.form.get("price"))
        total = quantity * price

        # Generate PDF
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Invoice/Bill")
        c.drawString(100, 720, f"Customer Name: {name}")
        c.drawString(100, 700, f"Email: {email}")
        c.drawString(100, 680, f"Product: {product}")
        c.drawString(100, 660, f"Quantity: {quantity}")
        c.drawString(100, 640, f"Price per Unit: {price}")
        c.drawString(100, 620, f"Total Amount: {total}")
        c.save()
        buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name="bill.pdf", mimetype="application/pdf")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
