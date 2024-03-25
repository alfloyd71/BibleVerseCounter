import pythonbible as bible
from .bible_book_chapters import *
#from quiz.views import *
import random
import string

def getRandomVerse(bookandchapter="Psalms 119", last_verse="176"):
    random_versenum=random.randint(1, int(last_verse))
    random_verse=bookandchapter+':'+str(random_versenum)
    return random_verse

def findLastVerse(text="1 tim 1"):
    versenotfound=False
    chapter=""
    bookandchapter=""
    try:
        references = bible.get_references(text)
    except:
        print("The verse you mentioned was not found in the Bible.")
        bookandchapter="Psalms 119"
        last_verse ="0"
        versenotfound=True
        return last_verse,versenotfound

    #example is 1 Timothy 1:1-20
    formatted_reference = bible.format_scripture_references(references)

    match (formatted_reference):
        case "Philemon 1":
            formatted_reference="Philemon 1:1-25"
        case "2 John 1":
            formatted_reference="2 John 1:1-13"
        case "3 John 1":
            formatted_reference="3 John 1:1-15"
        case "Jude 1":
            formatted_reference="Jude 1:1-25"
    
    if formatted_reference!="":#empty string if mistyped book in the Bible
    
        book_name=formatted_reference.split(' ')
        
        try:#if book_name starts with an Integer
            if (formatted_reference!="2 John 1:1-13" and formatted_reference!="3 John 1:1-15"):
                myint=int(book_name[0])
                bookname=book_name[1]
                chapter=book_name[2]

                match=""
                i=0
                while(match!=":"):
                    print(chapter[i])
                    match=chapter[i]
                    i+=1
            
                bookandchapter=str(myint)+' '+bookname+ ' '+ chapter[0:i-1]
       
        except:
            if (len(book_name)<=2):
                bkname=book_name[0]

                #parse chapter
                try:
                    chapter=book_name[1]
                except:
                    chapter="3:1-35"
                    formatted_reference="Matthew 3:0-0"
            else:
                #Song of Solomon
                if (book_name[0]=="Song"):
                    bkname=book_name[0]+" "+book_name[1]+" "+book_name[2] 
                    chapter=book_name[3]

            match=""
            i=0
            try:
              while(match!=":"):
                
                    match=chapter[i]
                
                    
                    i+=1
            except IndexError:
                chapter="3:1-35"
                formatted_reference="Matthew 3:0-0"
                    
                print("an IndexError has occurred")

            bookandchapter=bkname+ ' '+ chapter[0:i-1]

        #find last verse of all possible verses for that specific chapter in the Bible
        match=""
        i=0
        while(match!="-"):
            i-=1
            match=formatted_reference[i]
            

        last_verse=formatted_reference[i+1:]

    else:
        print("The verse you mentioned was not found in the Bible.")
        bookandchapter="Psalms 119"
        last_verse ="0"
        versenotfound=True

    return last_verse, versenotfound





