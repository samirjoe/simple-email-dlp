import email
import re

file_path = "/var/mail/admin"
with open(file_path, "r") as file:
	content = file.read()
	email_to_string = email.message_from_string(content)

	headers = email_to_string._headers
	
	header_contents = {}
	for header in headers:
		if "From" in header:
			header_contents['From'] = header[-1]
		elif "To" in header:
			header_contents['To'] = header[-1]
		elif "Date" in header:
			header_contents['Date'] = header [-1]
		elif "Subject" in header:
			header_contents['Subject'] = header[-1]
	
		
	if email_to_string.is_multipart():
		body = []
		for lines in body.get_payload():
			body.append(lines)
		body = " ".join(body)
	else:
		body = email_to_string.get_payload()


	
	print("HEADER CONTENTS\n", header_contents)
	#print("Break\n")
	print("BODY\n", body)
	
	if email_to_string.is_multipart():
		body = []
		for lines in body.get_payload():
			body.append(lines)
		body = " ".join(body)
	else:
		body = email_to_string.get_payload()	
	
	
	body = email_to_string.get_payload(decode=True)
	
	
	print("HEADER CONTENTS", header_contents)	
	print("decrypt")
	print("BODY\n",body)
	
