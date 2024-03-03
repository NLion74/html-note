import markdown
try:
    import importlib.resources
except ImportError:
    import importlib_resources

def main(note_markdown_file):
    note_title = fetch_note_title(note_markdown_file)
    note_html = convert_html(note_markdown_file)

    create_note(note_title, note_html)


def create_note(note_title, note_html):
    try:
        package = __package__
        if package is None:
            package = __name__

        with importlib.resources.path(package, "html") as p:
            html_base_content = open(f"{p}/base.html").read().split("{note_content}", 1)
    except Exception as e:
        print(f"Exception: {e}")
        return None

    with open(f"{note_title}.html", "w") as f:
        f.write(
            f"{html_base_content[0]}"
            f"{note_html}"
            f"{html_base_content[1]}"
        )


def fetch_note_title(markdown_note_path):
    """
    Add folder support
    Add support for multiple files divided by commas
    """

    note_title = markdown_note_path.split(".", 1)[0]
    return note_title


def convert_html(markdown_note):
    note_html = markdown.markdown(open(markdown_note, "r").read())
    return note_html

