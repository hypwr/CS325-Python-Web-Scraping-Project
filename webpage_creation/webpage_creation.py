from xml.etree import ElementTree as ET
import argparse

class OutputHTML():
    # parser that takes two arguments
    def parser(self):
        parser=argparse.ArgumentParser()
        parser.add_argument(help="contentFileName.txt",dest="file_name",type=str)
        parser.add_argument(help="summaryOutputFileName.html",dest="html_name",type=str)
        args = parser.parse_args()
        return args

    # This version of summaryHTMLoutput instead of being incorperated with the rest of the program, accepts a seperate input file that already includes the
    # titles and content in a similar fashion to that described in the scrape_output.py version of this function, ex: title,content,title,content,etc.
    # Instead of creating the output file from scratch, it accepts an output file.
    def summaryHTMLoutput(self, contentFile, outputFile)->None:

        with open(contentFile, 'r') as f:
            contentArray = f.readlines()

        # Iterations should be 1 per title and content, so length/2 should give us the required amount of iterations.
        iterations = int(len(contentArray)/2)
        pos = 0
        root = ET.Element("html")

        head = ET.SubElement(root, "head")
        title = ET.SubElement(root, "title")
        title.text = "Summary HTML Page"
        body = ET.SubElement(root, "body")

        # This segment iterates through the array length/2 times. 
        for i in range(iterations):
            header = contentArray[pos]
            paragraph = contentArray[pos+1]
            pos+=2

            h1 = ET.SubElement(body, "h1")
            h1.text = header
            p = ET.SubElement(body, "p")
            p.text = paragraph

        # Outputs the html to the given file.
        with open(outputFile,"wb") as f:
            tree = ET.ElementTree(root)
            tree.write(f, encoding="utf-8")
            f.close()
            
def main() -> None:
    HTMLobj = OutputHTML()
    # pulls arguments from the command line
    args=HTMLobj.parser()
    contentFile=args.file_name
    outputFile=args.html_name
    # outputs the data from the contentFile into the HTML outputFile.
    HTMLobj.summaryHTMLoutput(contentFile, outputFile)
    print("Finished Outputting Data To HTML File")

main()
