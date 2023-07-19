from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.platypus import TableStyle


pdfmetrics.registerFont(TTFont('microsoft.ttf', "./font/microsoft.ttf"))

titletbstyle = TableStyle([
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('FONTNAME', (0, 0), (-1, -1), 'microsoft.ttf'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), 
    ('ALIGN', (0, 0), (0, 3), 'RIGHT'),  
    ('ALIGN', (1, 0), (1, 3), 'LEFT'), 
    ('ALIGN', (2, 0), (2, 3), 'RIGHT'), 
    ('ALIGN', (3, 0), (3, 3), 'LEFT'),
    ('ALIGN', (4, 0), (4, 3), 'RIGHT'),
    ('ALIGN', (5, 0), (5, 3), 'LEFT'), 
])

columntbstyle = TableStyle([
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('FONTNAME', (0, 0), (-1, -1), 'microsoft.ttf'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.black),
    ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.black), 
    ('ALIGN', (0, 0), (2, 0), 'LEFT'),
    ('ALIGN', (3, 0), (5, 0), 'RIGHT'),
    ('ALIGN', (6, 0), (-1, -1), 'LEFT'),    
])

normaltbstyle = TableStyle([
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('FONTNAME', (0, 0), (-1, -1), 'microsoft.ttf'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), 
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'), 
    ('ALIGN', (3, 0), (5, -1), 'RIGHT'),
    ('LINEABOVE', (0, -1), (-1, -1), 2, colors.black), 
    ('LINEABOVE', (0, -1), (-1, -1), 0.5, colors.white),  
])