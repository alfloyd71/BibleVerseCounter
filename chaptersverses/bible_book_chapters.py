import pythonbible
import string

def getBookChapters(bookname="PSALMS"):
    """returns number of chapters for each book of the Bible that is specified inside variable bookname"""
    numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PSALMS)
    match bookname:
        # Old Testament – 929 chapters
        case "GENESIS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.GENESIS)
        case "EXODUS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.EXODUS)
        case "LEVITICUS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.LEVITICUS)
        case "NUMBERS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.NUMBERS)
        case "DEUTERONOMY" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.DEUTERONOMY)
        case "JOSHUA" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOSHUA)
        case "JUDGES" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JUDGES)
        case "RUTH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.RUTH)
        case "1 SAMUEL" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.SAMUEL_1)
        case "2 SAMUEL" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.SAMUEL_2)
        case "1 KINGS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.KINGS_1)
        case "2 KINGS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.KINGS_2)
        case "1 CHRONICLES" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.CHRONICLES_1)
        case "2 CHRONICLES" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.CHRONICLES_2)
        case "EZRA" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.EZRA)
        case "NEHEMIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.NEHEMIAH)
        case "ESTHER" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ESTHER)
        case "JOB" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOB)
        case "PSALM" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PSALMS)
        case "PSALMS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PSALMS)
        case "PROVERBS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PROVERBS)
        case "ECCLESIASTES" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ECCLESIASTES)
        case "SONG" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.SONG_OF_SONGS)
        case "SONG OF SOLOMON" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.SONG_OF_SONGS)
        case "ISAIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ISAIAH)
        case "JEREMIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JEREMIAH)
        case "LAMENTATIONS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.LAMENTATIONS)
        case "EZEKIEL" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.EZEKIEL)
        case "DANIEL" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.DANIEL)
        case "HOSEA" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.HOSEA)
        case "JOEL" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOEL)
        case "AMOS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.AMOS)
        case "OBADIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.OBADIAH)
        case "JONAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JONAH)
        case "MICAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.MICAH)
        case "NAHUM" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.NAHUM)
        case "HABAKKUK" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.HABAKKUK)
        case "ZEPHANIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ZEPHANIAH)
        case "HAGGAI" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.HAGGAI)
        case "ZECHARIAH" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ZECHARIAH)
        case "MALACHI" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.MALACHI)

        #New Testament – 260 chapters
        case "MATTHEW" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.MATTHEW)
        case "MARK" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.MARK)
        case "LUKE" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.LUKE)
        case "JOHN" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOHN)
        case "ACTS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ACTS)
        case "ROMANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.ROMANS)
        case "1 CORINTHIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.CORINTHIANS_1)
        case "2 CORINTHIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.CORINTHIANS_2)
        case "GALATIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.GALATIANS)
        case "EPHESIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.EPHESIANS)
        case "PHILIPPIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PHILIPPIANS)
        case "COLOSSIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.COLOSSIANS)
        case "1 THESSALONIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.THESSALONIANS_1)
        case "2 THESSALONIANS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.THESSALONIANS_2)
        case "1 TIMOTHY" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.TIMOTHY_1)
        case "2 TIMOTHY" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.TIMOTHY_2)
        case "TITUS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.TITUS)
        case "PHILEMON" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PHILEMON)
        case "HEBREWS" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.HEBREWS)
        case "JAMES" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JAMES)
        case "1 PETER" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PETER_1)
        case "2 PETER" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.PETER_2)
        case "1 JOHN" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOHN_1)
        case "2 JOHN" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOHN_2)
        case "3 JOHN" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JOHN_3)
        case "JUDE" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.JUDE)
        case "REVELATION" :
            numofchaps=pythonbible.get_number_of_chapters(pythonbible.Book.REVELATION)

        
    if str(numofchaps)=="150":
        if bookname!="PSALM" and bookname!="PSALMS":
            print("The book of "+bookname+ " was not found in the King James Bible.")
            return str(0)
        
    return str(numofchaps)
