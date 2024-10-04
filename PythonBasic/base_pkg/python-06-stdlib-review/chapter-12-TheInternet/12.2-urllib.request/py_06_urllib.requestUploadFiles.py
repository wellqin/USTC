"""
! what?
MIME types (IANA media types)
A media type (also known as a Multipurpose Internet Mail Extensions or MIME type)

MIME is an industry email standard. 
Many email applications create messages in MIME format and save them in files with the .EML extension.

MIME is a standard used by internet email 
to transmit the following types of content via SMTP:
- Plain text message
- Message with alternative content (i.e., in both plain text and HTML)
- Reply message with the original message attached
- Text message with attachments of image, audio, video, or application files
- Other message constructs

The following are typical MIME headers in a message. 
For more information, see RFC 2045.
- MIME-Version - Indicates the message is MIME-formatted.
- Content-Type - Indicates the media type of the message or a part of the message, represented by a type and subtype. 
  It also includes a boundary field which specifies a string as the MIME boundary or as the encapsulation boundary, depending on the location of Content-Type.
- Content-Disposition - Provides details of an attachment such as its presentation style (inline or attachment), filenames, and creation and last modification dates.
- Content-Transfer-Encoding - Specifies the encoding method to represent binary data.


! why?
why not?
we have a industry email standard. good

! how?
link: https://docs.microsoft.com/en-us/graph/outlook-get-mime-message#:~:text=MIME%20is%20a%20standard%20used%20by%20internet%20email,video%2C%20or%20application%20files%205%20Other%20message%20constructs

"""

import io
import mimetypes
from urllib import request
import uuid

class MultiPartForm:
    """Accumulate the data to be used when posting a form."""
    def __init__(self):
        self.form_fields = []
        self.files = []
        # Use a large random byte string to separate
        # parts of the MIME data.
        self.boundary = uuid.uuid4().hex.encode('utf-8')
        return
    def get_content_type(self):
        return 'multipart/form-data; boundary={}'.format(
        self.boundary.decode('utf-8'))
    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
    def add_file(self, fieldname, filename, fileHandle,
                mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = (
                mimetypes.guess_type(filename)[0] or
                'application/octet-stream'
            )
        self.files.append((fieldname, filename, mimetype, body))
        return
    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; '
            'name="{}"\r\n').format(name).encode('utf-8')
    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Disposition: file; '
            'name="{}"; filename="{}"\r\n').format(
                name, filename).encode('utf-8')
    @staticmethod
    def _content_type(ct):
        return 'Content-Type: {}\r\n'.format(ct).encode('utf-8')
    def __bytes__(self):
        """Return a byte-string representing the form data,
        including attached files.
        """
        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'
        # Add the form fields.
        for name, value in self.form_fields:
            buffer.write(boundary)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')
        # Add the files to upload.
        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(f_name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')
        buffer.write(b'--' + self.boundary + b'--\r\n')
        return buffer.getvalue()

if __name__ == '__main__':
    # Create the form with simple fields.
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')
    # Add a fake file.
    form.add_file(
        'biography', 'bio.txt',
        fileHandle=io.BytesIO(b'Python developer and blogger.'))
    # Build the request, including the byte-string
    # for the data to be posted.
    data = bytes(form)
    r = request.Request('http://localhost:8080/', data=data)
    r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
    )
    r.add_header('Content-type', form.get_content_type())
    r.add_header('Content-length', len(data))
    print()
    print('OUTGOING DATA:')
    for name, value in r.header_items():
        print('{}: {}'.format(name, value))
    print()
    print(r.data.decode('utf-8'))
    print()
    print('SERVER RESPONSE:')
    print(request.urlopen(r).read().decode('utf-8'))