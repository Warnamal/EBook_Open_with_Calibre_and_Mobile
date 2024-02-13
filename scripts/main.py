import os
import re
import subprocess
import logging
from datetime import datetime
from ebooklib import epub
from PIL import Image

log_folder = "C:\\tmp\\EbookCreation\\logs"
log_file_name = f"EbookCreation_{datetime.now().strftime('%Y%m%d_%H%M')}.log"
log_file_path = os.path.join(log_folder, log_file_name)

os.makedirs(log_folder, exist_ok=True)

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def create_metadata(book):
    book.set_identifier('Adyathana2(WasanthaKKGee)')
    book.set_title('Adyathana2(WasanthaKKGee)')
    book.set_language('si')
    book.add_author('Samudra Weththasinhe')

def create_cover(book, src_folder, max_width=320, max_height=640):
    # Look for an image in the specified directory
    cover_path = None
    jpg_folder = "C:\\tmp\\EbookCreation\\input\\jpg"
    for file in os.listdir(jpg_folder):
        if file.startswith("000") and file.lower().endswith(('.png', '.jpg', '.jpeg')):
            cover_path = os.path.join(jpg_folder, file)
            break

    if cover_path:
        try:
            # Open the cover image using PIL
            with Image.open(cover_path) as img:
                # Resize the image while preserving aspect ratio
                img.thumbnail((max_width, max_height))
                # Convert to RGB if not already
                img = img.convert('RGB')
                # Save the resized image to a temporary file
                resized_cover_path = os.path.join(src_folder, 'resized_cover.jpg')
                img.save(resized_cover_path)

            # Add the resized cover to the EPUB
            cover_item = epub.EpubItem(file_name=resized_cover_path, media_type='image/jpeg')
            book.add_item(cover_item)

            # Set the cover image in the EPUB metadata
            book.set_cover('cover.jpg', open(resized_cover_path, 'rb').read())

            # Remove the temporary resized cover file
            os.remove(resized_cover_path)

        except Exception as e:
            logging.warning(f"Error setting cover image: {str(e)}")
    else:
        # Create default cover with book title in English and Sinhala
        logging.warning("No image starting with '000' found in the directory. Creating default cover.")
        cover_content = '\n'.join(['Adyathana2(WasanthaKKGee)', 'Default Cover'])
        cover_item = epub.EpubItem(content=cover_content.encode('utf-8'), media_type='text/plain')
        book.add_item(cover_item)

def create_css(book):
    css_content = '''
    body {
        font-size: 40%;
        line-height: 1; /* Adjust the line height as needed */
    }
    '''
    css_item = epub.EpubItem(content=css_content, file_name='styles.css', media_type='text/css')
    book.add_item(css_item)

def create_chapter_item(content, i):
    chapter_id = f"chapter_{i + 1}"
    chapter_filename = f"{chapter_id}.xhtml"

    # Ensure content is XHTML compliant
    if isinstance(content, str):
        # Split the content into lines
        lines = content.split('\n')
        
        # Bold the first line and increase font size
        lines[0] = f"<b><span style='font-size: 120%;'>{lines[0]}</span></b>"
        
        # Join the lines back together
        content_with_br = '<br>\n'.join(lines)
        
        # Replace newline characters with <br> tags
        content_with_br = content_with_br.replace('\n', '<br>\n')

        content_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter {i + 1}</title>
</head>
<body>
    <div>{content_with_br}</div>
</body>
</html>'''
    else:
        content_xhtml = ''

    return epub.EpubItem(content=content_xhtml.encode('utf-8'), file_name=chapter_filename,
                         media_type='application/xhtml+xml', uid=chapter_id)

def create_epub(src_folder, dest_folder):
    try:
        # Check if the source directory exists and is not empty
        if not os.path.exists(src_folder) or not os.path.isdir(src_folder) or not os.listdir(src_folder):
            print(f"Error: Source directory '{src_folder}' does not exist, is not a valid directory, or is empty.")
            return

        # Check if the output directory exists, create if not
        os.makedirs(dest_folder, exist_ok=True)

        # Check if the EPUB file already exists in the output directory
        epub_file_path = os.path.join(dest_folder, 'Adyathana2(WasanthaKKGee).epub')
        if os.path.exists(epub_file_path):
            print(f"EPUB file '{epub_file_path}' already exists. Skipping creation.")
            return

        # Create EPUB book
        book = epub.EpubBook()

        # Create metadata
        create_metadata(book)

        # Create or copy cover image
        create_cover(book, src_folder)

        # Create CSS style for reducing font size and line spacing
        create_css(book)

        # Create individual XHTML files for each text file
        chapters = []
        for i, txt_file in enumerate(sorted(os.listdir(src_folder))):
            if not txt_file.endswith('.txt'):
                continue

            txt_path = os.path.join(src_folder, txt_file)
            with open(txt_path, 'r', encoding='utf-8') as f:
                content = f.read()
                chapter_item = create_chapter_item(content, i)
                chapters.append(chapter_item)

        # Add chapters to the book
        for chapter in chapters:
            book.add_item(chapter)

        # Set the spine
        book.spine = [item for item in chapters]

        # Create table of contents
        toc_item = epub.EpubItem(uid="toc", file_name="toc.xhtml", media_type="application/xhtml+xml")
        book.add_item(toc_item)
        book.toc = [toc_item]

        # Write EPUB file
        epub_file_path = os.path.join(dest_folder, 'Adyathana2(WasanthaKKGee).epub')
        epub.write_epub(epub_file_path, book)

        logging.info(f"EPUB file '{epub_file_path}' created successfully.")

        # Print a message to the command line
        print(f"EPUB file '{epub_file_path}' created successfully.")

        # Open the EPUB file with Calibre's ebook-viewer
        calibre_path = r'C:\Program Files\Calibre2\calibre.exe'  # Update the path accordingly
        subprocess.Popen([calibre_path, 'view', epub_file_path])  # Modified to use Popen

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    src_folder = "C:\\tmp\\EbookCreation\\input\\Adyathana2(WasanthaKKGee)-SamudraW"
    dest_folder = "C:\\tmp\\EbookCreation\\outputs"  # Update the output directory accordingly

    create_epub(src_folder, dest_folder)
