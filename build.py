import shutil
from pathlib import Path
import datetime
import markdown

cont_dir = Path("content")
blog_dir = Path("content/blog")
temp_dir = Path("templates")
stat_dir = Path("static")
site_dir = Path("site")

base_temp = (temp_dir / "base.html").read_text(encoding="utf-8")
page_temp = (temp_dir / "page.html").read_text(encoding="utf-8")
post_temp = (temp_dir / "post.html").read_text(encoding="utf-8")
blog_temp = (temp_dir / "blog.html").read_text(encoding="utf-8")

def render(body, title):
    result = base_temp.replace("{{ title }}", title)
    result = result.replace("{{ content }}", body)
    return result

def convert(path):
    md = markdown.Markdown(extensions=["meta", "fenced_code", "tables"])
    html = md.convert(Path(path).read_text(encoding="utf-8"))
    return (html, md.Meta)