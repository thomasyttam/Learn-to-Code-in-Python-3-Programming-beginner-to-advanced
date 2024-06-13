# Description: This program extracts the country code, product code, and batch number from a lot number.

lotNumber = "037-00901-00027"
print("Country Code: " + lotNumber[:3])
print("Product Code: " + lotNumber[4:9])
print("Batch Number: " + lotNumber[10:])