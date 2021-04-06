import PyPDF2


magazines = [
"BB-2011-01-22.pdf",
"BB-2010-01-16.pdf",
"BB-2010-01-23.pdf",
"BB-2010-01-30.pdf",
"BB-2010-02-06.pdf",
"BB-2010-02-12.pdf",
"BB-2010-02-13.pdf",
"BB-2010-02-20.pdf",
"BB-2010-02-27.pdf",
"BB-2010-03-06.pdf",
"BB-2010-03-13.pdf",
"BB-2010-03-20.pdf",
"BB-2010-03-27.pdf",
"BB-2010-04-02.pdf",
"BB-2010-04-03.pdf",
"BB-2010-04-10.pdf",
"BB-2010-04-16.pdf",
"BB-2010-04-17.pdf",
"BB-2010-04-24.pdf",
"BB-2010-04-30.pdf",
"BB-2010-05-01.pdf",
"BB-2010-05-08.pdf",
"BB-2010-05-14.pdf",
"BB-2010-05-15.pdf",
"BB-2010-05-22.pdf",
"BB-2010-05-29.pdf",
"BB-2010-06-05.pdf",
"BB-2010-06-12.pdf",
"BB-2010-06-19.pdf",
"BB-2010-06-26.pdf",
"BB-2010-07-03.pdf",
"BB-2010-07-10.pdf",
"BB-2010-07-17.pdf",
"BB-2010-07-24.pdf",
"BB-2010-07-31.pdf",
"BB-2010-08-07.pdf",
"BB-2010-08-14.pdf",
"BB-2010-08-21.pdf",
"BB-2010-08-28.pdf",
"BB-2010-09-04.pdf",
"BB-2010-09-11.pdf",
"BB-2010-09-18.pdf",
"BB-2010-09-25.pdf",
"BB-2010-10-02.pdf",
"BB-2010-10-09.pdf",
"BB-2010-10-16.pdf",
"BB-2010-10-23.pdf",
"BB-2010-10-30.pdf",
"BB-2010-11-06.pdf",
"BB-2010-11-13.pdf",
"BB-2010-11-20.pdf",
"BB-2010-11-27.pdf",
"BB-2010-12-04.pdf",
"BB-2010-12-11.pdf",
"BB-2010-12-18.pdf",
"BB-2010.pdf",
"BB2010.pdf",


]

albums = [
"Letiště",
"Vida artificial",
"Cure for Your Disease",
"Pulse",
"Tierra",
"Kompromisy",
"Mil martillazos de ira",
"Crawling Out of Hell",
"The Fundamentally Lost World",
"Promise Land",
"Set in Stone",
"Evolution",
"Overdrive",
"Forevermore",
"Evidence",
"As a Dog Returns",
"Lords of Torment",
"Sabre",
"Gorgoni",
"Taste the Sin Through the Fire",
"Revolution 2.0",
"Filthy Lucre",
"Second Coming, Second Crucifixion",
"The Bride Screamed Murder",
"Fragments",
"Prepared for Discharge",
"No Escape",
"Fighter",
"Inferno of Sacred Destruction",
"Unfinished Business",
"The Clans Will Rise Again",
"Road to the Octagon",
"Leviathan Destroyer",
"Darkly, Darkly, Venus Aversa",
"Counting Our Scars",
"Black Masses",
"From Ashes to Madness",
]

for m in magazines:
    with open('band.txt', 'a' ) as file:
        file.write("This is the " + m + " magazine issue"  '\n')
    pdfFileObj = open('2010mags/'+ m , 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for page_num in range(pdfReader.numPages):
        page_obj = pdfReader.getPage(page_num)
        text = page_obj.extractText()
        for a in albums:
            if a in text:
                with open('band.txt', 'a' ) as file:
                    file.write("Found " + a + " on page " + str(page_num) +  '\n')      
    pdfFileObj.close()

