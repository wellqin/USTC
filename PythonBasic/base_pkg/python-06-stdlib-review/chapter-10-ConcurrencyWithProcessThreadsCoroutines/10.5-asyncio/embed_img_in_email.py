"""
! what?
to enhance readability and UX in email manner,
it recommends to display all info from email attachment to email body. because no one f*cuking likes to open tens thounds of attachement to read. 
email receivers are numble.

`single-threaded, visual creature heh`

! why?
i'm tired of opening powerpoint materials, doing screenshot, and pasting into email ect, it's f*cking pain in ass

! how?

only works on smtplib tho ..
Didnt find a good solution for Office Outlook application fuck
link: https://stackoverflow.com/questions/920910/sending-multipart-html-emails-which-contain-embedded-images
"""

from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import win32com.client as win32

msg = EmailMessage()

# generic email headers
msg['Subject'] = 'hello there'
msg['From']    = 'liang.zhang@sony.com'
msg['To']      = 'liang.zhang@sony.com'

# set the pain text body
msg.set_content('This is a plain text body.')
# now create a Content-ID for the image
image_cid = make_msgid(domain='liang.zhang@sony.com')

# set an alternative html body
# image_cid looks like <long.random.number@xyz.com>
# to use it as the img src, we don't need `<` or `>`
# so we use [1:-1] to strip them off
msg.add_alternative(
    """
    <html>
        <body>
            <p>
                This is an HTML body. <br>
                It also havs an image.
            </p>
            <img src="cid:{img_cid}">
        </body>
    </html>
    """.format(img_cid=image_cid[1:-1]),
    subtype='html',
)

img_path = r'C:\Users\5106001995\Pictures\Cpk_To_PPM.jpg'
with open(img_path, 'rb') as img:
    # know the content-type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
    # attach it
    msg.get_payload()[1].add_related(
        img.read(),
        maintype=maintype,
        subtype=subtype,
        cid=image_cid,
    )

# the message is ready now
# you can write it to a file
# or send it using smtplib

# create Outloop application
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0x0)
mail.To = 'liang.zhang@sony.com'
mail.Subject = 'test'
mail.Send()