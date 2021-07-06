user =input("enter your name : ")
user_edit= user.replace(" ","")
company= input("enter your company name : ")
company_edit=company.replace(" ","")
email = user_edit + '@' + company_edit + ".com"
email_edit = email.lower()
print("your email Id is", email_edit)
