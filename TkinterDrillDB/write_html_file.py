#this module writes a file with an html extension in the cwd


class WriteHtmlFile:

    def __init__(self):
        html_body = ''
        html_page = ''

    def set_html_text(self, txt="Welcome to our Summer Sale!"):
        self.html_body = txt

    def format_html(self):
        self.html_page = ('<html>\n', '<body>\n', '{}\n'.format(self.html_body), '</body>\n', '</html>\n')


    def write_the_file(self, filename="abcsale.html"):
        f = open(filename, "w+")
        for line in self.html_page:
            f.write("%s" % line)
        f.close()
 

def main():
    write_html = WriteHtmlFile()
    write_html.set_html_text()
    write_html.format_html()
    write_html.write_the_file()

   
if __name__ == "__main__": main()

