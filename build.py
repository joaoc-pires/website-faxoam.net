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
    result = base_temp.replace("{{ title }}", title).replace("{{ content }}", body)
    return result

def convert(path):
    md = markdown.Markdown(extensions=["meta", "fenced_code", "tables"])
    html = md.convert(Path(path).read_text(encoding="utf-8"))
    return (html, md.Meta)

def clear_directories():
    if site_dire.exists():
        shutil.rmtree(site_dir)
    site_dir.mkdir(parents=True, exists_ok=True)

def make_about():
    html, meta = convert(cont_dir / "about.md")
    body = page_temp.replace("{{ title }}"), meta["title"][0].replace("{{  content  }}", html)
    about_dir = site_dir / "about"
    about_dir.mkdir(parents=True, exists_ok=True)
    (about_dir / "index.html").write_text(render(body, meta["title"][0]), encoding="utf-8")

def make_blog_posts():
    posts = []
    for file in blog_dir.glob("*.md"):
        html, meta = convert(file)
        slug = file.stem[11:]
        date = meta["date"][0]
        title = meta["title"][0]
        body = post_temp.replace("{{ title }}", title).replace("{{ date }}", date).replace("{{ content }}", html)
        post_dir = site_dir / "blog" / slug
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.html").write_text(render(body, title), encoding="utf-8")
        posts.append({"title": title, "date": date, "slug": slug, "html": html})
    
    posts.sort(key=lambda p: p["date"], reverse=True)

clear_directories()
make_about()
make_blog_posts()