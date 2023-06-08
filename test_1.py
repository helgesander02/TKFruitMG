import os, sys
import win32print
printer_name = win32print.GetDefaultPrinter ()
drivers = win32print.EnumPrinterDrivers(None, None, 2)
hPrinter = win32print.OpenPrinter(printer_name)
printer_info = win32print.GetPrinter(hPrinter, 2)
for driver in drivers:
    if driver["Name"] == printer_info["pDriverName"]:
        printer_driver = driver
raw_type = "XPS_PASS" if printer_driver["Version"] == 4 else "RAW"
raw_data = "This is a test"
try:
  hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, raw_type))
  try:
    win32print.StartPagePrinter(hPrinter)
    win32print.WritePrinter(hPrinter, raw_data.encode())
    win32print.EndPagePrinter(hPrinter)
  finally:
    win32print.EndDocPrinter(hPrinter)
finally:
  win32print.ClosePrinter(hPrinter)