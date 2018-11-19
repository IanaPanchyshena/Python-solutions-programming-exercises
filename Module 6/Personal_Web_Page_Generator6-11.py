# Personal_Web_Page_Generator6-11

# Write a program that asks the user for his or her name,
# then asks the user to enter a sentence that describes himself or herself.
# Here is an example of the program’s screen:
# Enter your name: Julie Taylor
# Describe yourself: I am a computer science major, a member of the Jazz club,
# and I hope to work as a mobile app developer after I graduate.

# Once the user has entered the requested input,
# the program should create an HTML file, containing the input,
# for a simple Web page.
# Here is an example of the HTML content, using the sample input previously shown:
#    <html>
#    <head>
#    </head>
#    <body>
#        <center>
#            <h1>Julie Taylor</h1>
#        </center>
#        <hr />
#        I am a computer science major, a member of the Jazz club,
#        and I hope to work as a mobile app developer after I graduate.
#        <hr />
#    </body>
#    </html>

def main():
    name=input('Enter your name: ')
    describe=input('Describe yourself: ')

    file=open('webPage.html','w')

    file.write('<html>\n')
    file.write('<head>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('\t<center>\n')
    file.write('\t\t<h1>'+name+'</h1>\n')
    file.write('\t</center>\n')
    file.write('\t<hr />\n')
    file.write('\t'+describe+'\n')
    file.write('\t<hr />\n')
    file.write('</body>\n')
    file.write('</html>\n')

    file.close()

main()
            
