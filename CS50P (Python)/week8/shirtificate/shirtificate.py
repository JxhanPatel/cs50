from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 15, 60, 200)
        self.set_font("helvetica", "", 50)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 212, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    shirt(name)

if __name__ == "__main__":
    main()
