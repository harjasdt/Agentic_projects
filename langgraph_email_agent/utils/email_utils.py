
import os
import shutil
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
from mimetypes import guess_type as guess_mime_type
import os
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# utility functions
def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def parse_parts(service, parts, folder_name, message):
    """
    Utility function that parses the content of an email partition
    """
    text=''
    if parts:
        for part in parts:
            filename = part.get("filename")
            mimeType = part.get("mimeType")
            print(mimeType,'###')
            body = part.get("body")
            data = body.get("data")
            file_size = body.get("size")
            part_headers = part.get("headers")
            
            if part.get("parts"):
                # recursively call this function when we see that a part
                # has parts inside
                parse_parts(service, part.get("parts"), folder_name, message)
            if mimeType == "text/plain":
                # if the email part is text plain
                if data:
                    text += urlsafe_b64decode(data).decode()
                    # print(text,filename)
                    
            elif mimeType == "text/html":
                # if the email part is an HTML content
                # save the HTML file and optionally open it in the browser
                if not filename:
                    filename = "index.html"
                filepath = os.path.join(folder_name, filename)
                print("Saving HTML to", filepath)
                with open(filepath, "wb") as f:
                    f.write(urlsafe_b64decode(data))
            else:
                print("Unknown MIME type:", mimeType)
                # attachment other than a plain text or HTML
                for part_header in part_headers:
                    part_header_name = part_header.get("name")
                    part_header_value = part_header.get("value")
                    if part_header_name == "Content-Disposition":
                        if "attachment" in part_header_value:
                            # we get the attachment ID 
                            # and make another request to get the attachment itself
                            print("Saving the file:", filename, "size:", get_size_format(file_size))
                            attachment_id = body.get("attachmentId")
                            attachment = service.users().messages() \
                                        .attachments().get(id=attachment_id, userId='me', messageId=message['id']).execute()
                            data = attachment.get("data")
                            filepath = os.path.join(folder_name, filename)
                            if data:
                                with open(filepath, "wb") as f:
                                    f.write(urlsafe_b64decode(data))

    # return text

    




def extract_all_text_from_folder(folder_path: str) -> str:
    """
    Extracts text from all HTML and PDF files in a folder.
    
    Args:
        folder_path (str): Path to the folder.

    Returns:
        str: Combined readable text content from all files.
    """
    combined_text = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Handle HTML files
        if filename.lower().endswith(".html"):
            with open(file_path, "r", encoding="utf-8") as f:
                html_content = f.read()
                soup = BeautifulSoup(html_content, "html.parser")

                # Extract plain text
                plain_text = soup.get_text(separator='\n', strip=True)

                # Extract tables
                table_text_parts = []
                for table in soup.find_all("table"):
                    table_text_parts.append("Table:")
                    for tr in table.find_all("tr"):
                        cells = tr.find_all(["th", "td"])
                        row_text = " | ".join(cell.get_text(strip=True) for cell in cells)
                        if row_text:
                            table_text_parts.append(row_text)

                file_text = plain_text + "\n\n" + "\n".join(table_text_parts)
                combined_text.append(f"----- {filename} -----\n{file_text}")

        # Handle PDF files
        elif filename.lower().endswith(".pdf"):
            try:
                with fitz.open(file_path) as pdf:
                    pdf_text = ""
                    for page in pdf:
                        pdf_text += page.get_text()
                combined_text.append(f"----- {filename} -----\n{pdf_text.strip()}")
            except Exception as e:
                combined_text.append(f"----- {filename} -----\n[Error reading PDF: {e}]")

    return "\n\n".join(combined_text)



import os
import shutil

def clean(text):
    # Removes invalid characters from folder/file names
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in text).strip()

def read_message(service, message):
    email_from = ""
    subject = ""
    email_content = f"THREAD_ID: {message['threadId']} \nMESSAGE_ID: {message['id']}\n"

    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    payload = msg['payload']
    headers = payload.get("headers")
    parts = payload.get("parts")

    folder_name = "email"  # default folder name
    has_subject = False

    if headers:
        for header in headers:
            name = header.get("name")
            value = header.get("value")
            if name.lower() == "from":
                email_from = value
                email_content += f"From: {value}\n"
            elif name.lower() == "to":
                email_content += f"To: {value}\n"
            elif name.lower() == "subject":
                has_subject = True
                subject = value
                folder_name = clean(value) or "email"
                folder_counter = 0
                original_name = folder_name
                while os.path.isdir(folder_name):
                    folder_counter += 1
                    folder_name = f"{original_name}_{folder_counter}"
                print("Subject:", subject)
                email_content += f"Subject: {subject}\n"
            elif name.lower() == "date":
                email_content += f"Date: {value}\n"

    # ✅ Ensure folder exists
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)

    # ✅ Now safely parse parts
    parsed_body_path = parse_parts(service, parts, folder_name, message)
    all_text = extract_all_text_from_folder(folder_name)
    email_content += all_text

    # ✅ Clean up folder
    shutil.rmtree(folder_name, ignore_errors=True)

    return email_content, email_from, subject
