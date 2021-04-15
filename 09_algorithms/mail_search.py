def mail_search(email, mails):
    for email in mails:
        if email == mails:
            return True
        else:
            return False


mails_list = ['a@a.pl', 'b@b.pl', 'c@c.pl']

searched_mail = 'b@b.pl'

print(mail_search(mails_list, searched_mail))