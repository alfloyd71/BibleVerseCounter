from django.shortcuts import render
from .bible_book_chapters import getBookChapters
from .getlastverse import findLastVerse
from django.http import HttpResponseRedirect
from chaptersverses.forms import BookChaptersVersesForm
import string, re
from .names_abbreviated import getBookNamesAbbreviated

# Create your views here.

def getNumberOfChaptersVerses(request):
    is_bookandchapter=True
    versenotfound=False
    notdefaultbookandchapter=True
    notdefaultbook=True
    bookandchapter="psalm 119"
    bookandchapter_bookname="psalm"
    bookandchapter_chapter="119"
    lastverse="176"
    versefound=True
    bookname="psalms"
    name="psalms"
    name=name.upper()
    numofchaps=int(getBookChapters(bookname=name))
    form=BookChaptersVersesForm()

    if request.method == 'POST':
        if "bookname" in request.POST:
            bookname=request.POST['bookname']
            bookname=bookname.strip()
            bookname=getBookNamesAbbreviated(bookname=bookname)
            bookname=bookname.upper()
            numofchaps=int(getBookChapters(bookname=bookname))
            is_bookandchapter=False
        if "bookandchapter" in request.POST:
            bookandchapter=request.POST['bookandchapter']
            lst=bookandchapter.split()
            if "bookname" in request.POST:
              if request.POST['bookname']=="":
                bookandchapter_bookname=lst[0]
                bookandchapter_chapter=lst[1]
              else:
                  bookandchapter_bookname="psalm"
                  bookandchapter_chapter="119"
            bookandchapter_bookname=bookandchapter_bookname.strip()
            bookandchapter_bookname=getBookNamesAbbreviated(bookname=bookandchapter_bookname)
            bookandchapter_bookname=bookandchapter_bookname.upper()
            pattern = r'^\d+\s+\w+\s+\d+'
            text = "2 Peter 3:8"
            match = re.match(pattern, bookandchapter)
            if(not match):
              bookandchapter=bookandchapter_bookname+" "+bookandchapter_chapter
            
            lastverse,versenotfound=findLastVerse(text=bookandchapter)


        return HttpResponseRedirect('?submitted=True&bookname=%s&bookandchapter=%s&lastverse=%s&versenotfound=%s' % (bookname, bookandchapter, lastverse, versenotfound))
    else:

        if "submitted" in request.GET:
            if("bookname" in request.GET):
                bookname=request.GET['bookname']
                bookname=bookname.strip()
            if bookname=="":
                notdefaultbook=False
            bookandchapter=request.GET['bookandchapter']
            if bookandchapter=="":
                notdefaultbookandchapter=False
            lastverse=request.GET['lastverse']
            versenotfound=request.GET['versenotfound']
            if lastverse=="177":
                versefound=False

        name=bookname
        name=name.upper()
        numofchaps=int(getBookChapters(bookname=name))

    name=string.capwords(name)
    bookandchapter=string.capwords(bookandchapter)
    context={'numofchaps':numofchaps,'form':form,'bookname':name,'bookandchapter':bookandchapter,
             'lastverse':lastverse, 'versefound':versefound, 'notdefaultbookandchapter':notdefaultbookandchapter,
             'notdefaultbook':notdefaultbook,'versenotfound':versenotfound}
    return render(request, "chaptersverses/kjvchaptersverses.html",context)
