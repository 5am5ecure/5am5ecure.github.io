import cgi

print("Testing")

form = cgi.FieldStorage()

first_input=form.getvalue('fInput')
second_input=form.getvalue('sInput')

print("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Testing - Python CGI Script</title>")
print ("</head>")
print ("<body>")
print ("<h1>Inputted strings: {} {}</h1>".format(first_input, second_input))
print ("</body>")
print ("</html>")
