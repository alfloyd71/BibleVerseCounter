from django.shortcuts import render
from .bible_book_chapters import getBookChapters
from .getlastverse import findLastVerse
from django.http import HttpResponseRedirect
from chaptersverses.forms import BookChaptersVersesForm
import string
from .names_abbreviated import getBookNamesAbbreviated

# Create your views here.

def getNumberOfChaptersVerses(request):
    versenotfound=False
    notdefaultbookandchapter=True
    notdefaultbook=True
    bookandchapter="psalm 119"
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

        bookandchapter=request.POST['bookandchapter']
        name=bookname
        name=name.upper()
        numofchaps=int(getBookChapters(bookname=name))
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
