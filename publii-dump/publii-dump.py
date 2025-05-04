#!/usr/bin/env python3
import os
import sys
import json
import sqlite3
import argparse
from pathlib import Path
from shutil import copyfile

ASCII_ART = r"""

 ▄▄▄·▄• ▄▌▄▄▄▄· ▄▄▌  ▪  ▪  ·▄▄▄▄  ▄• ▄▌• ▌ ▄ ·.  ▄▄▄·
▐█ ▄██▪██▌▐█ ▀█▪██•  ██ ██ ██▪ ██ █▪██▌·██ ▐███▪▐█ ▄█
 ██▀·█▌▐█▌▐█▀▀█▄██▪  ▐█·▐█·▐█· ▐█▌█▌▐█▌▐█ ▌▐▌▐█· ██▀·
▐█▪·•▐█▄█▌██▄▪▐█▐█▌▐▌▐█▌▐█▌██. ██ ▐█▄█▌██ ██▌▐█▌▐█▪·•
.▀    ▀▀▀ ·▀▀▀▀ .▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀•  ▀▀▀ ▀▀  █▪▀▀▀.▀   
	                	               v0.1.0

"""

parser = argparse.ArgumentParser(description="Exports content from a Publii SQLite database into structured folders.")
parser.add_argument("db", help="Path to the db.sqlite file")
parser.add_argument("--output", default="./output", help="Output directory (default: ./output)")
parser.add_argument("--ids", help="Comma-separated list of post IDs")
parser.add_argument("--no-tags", action="store_true", help="Do not export tags")
parser.add_argument("--no-authors", action="store_true", help="Do not export authors")
parser.add_argument("--no-images", action="store_true", help="Do not export images")
args = parser.parse_args()

print(ASCII_ART)

DB_PATH = args.db
OUTPUT_DIR = args.output
IDS = args.ids
NO_TAGS = args.no_tags
NO_AUTHORS = args.no_authors
NO_IMAGES = args.no_images

if NO_AUTHORS:
    print("⚠️  Author export is disabled (--no-authors)")
if NO_TAGS:
    print("⚠️  Tag export is disabled (--no-tags)")
if NO_IMAGES:
    print("⚠️  Image export is disabled (--no-images)")

if not os.path.isfile(DB_PATH):
    print(f"❌ SQLite file not found: {DB_PATH}")
    sys.exit(1)

PROJECT_DIR = Path(DB_PATH).parent
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_json(s):
    try:
        return json.loads(s)
    except:
        return s

def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def is_file(path):
    try:
        return Path(path).is_file()
    except:
        return False

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

count_posts = count_posts_published = count_posts_drafts = 0
count_pages = count_pages_published = count_pages_drafts = 0
count_featured_images = count_featured_missing = 0
count_inline_images = count_inline_missing = 0
count_authors = count_tags = 0
missing_featured = []
missing_inline = []

author_map = {}
if not NO_AUTHORS:
    for row in cur.execute("SELECT id, username FROM authors"):
        author_map[row["id"]] = row["username"]

tag_map = {}
post_tags = {}
if not NO_TAGS:
    for row in cur.execute("SELECT id, slug FROM tags"):
        tag_map[row["id"]] = row["slug"]
    for row in cur.execute("SELECT post_id, tag_id FROM posts_tags"):
        post_tags.setdefault(row["post_id"], []).append(row["tag_id"])

# Export authors
if not NO_AUTHORS:
    os.makedirs(f"{OUTPUT_DIR}/authors", exist_ok=True)
    for a in cur.execute("SELECT * FROM authors"):
        count_authors += 1
        obj = {
            "name": a["name"],
            "username": a["username"],
            "password": a["password"],
            "config": parse_json(a["config"] or "{}"),
            "additional_data": parse_json(a["additional_data"] or "{}")
        }
        write_json(f"{OUTPUT_DIR}/authors/{a['username']}.json", obj)
        print(f"👤 authors/{a['username']}.json ({a['name']})")

# Export tags
if not NO_TAGS:
    os.makedirs(f"{OUTPUT_DIR}/tags", exist_ok=True)
    for t in cur.execute("SELECT * FROM tags"):
        count_tags += 1
        obj = {
            "name": t["name"],
            "slug": t["slug"],
            "description": t["description"],
            "additional_data": parse_json(t["additional_data"] or "{}")
        }
        write_json(f"{OUTPUT_DIR}/tags/{t['slug']}.json", obj)
        print(f"🏷️  tags/{t['slug']}.json ({t['name']})")

# Additional post data
post_add = {}
for row in cur.execute("SELECT * FROM posts_additional_data"):
    post_add.setdefault(row["post_id"], {})[row["key"]] = parse_json(row["value"])

# Images
images = {}
if not NO_IMAGES:
    for row in cur.execute("SELECT * FROM posts_images"):
        images[row["id"]] = {
            "post_id": row["post_id"],
            "url": row["url"],
            "title": row["title"],
            "caption": row["caption"],
            "additional_data": parse_json(row["additional_data"] or "{}")
        }

# Process posts
query = "SELECT * FROM posts"
if IDS:
    query += f" WHERE id IN ({IDS})"
for post in cur.execute(query):
    pid = post["id"]
    slug = post["slug"]
    is_page = "is-page" in (post["status"] or "")
    is_published = "published" in (post["status"] or "")
    type_dir = "pages" if is_page else "posts"
    status_dir = "published" if is_published else "drafts"
    target_dir = Path(OUTPUT_DIR) / type_dir / status_dir
    target_dir.mkdir(parents=True, exist_ok=True)

    if is_page:
        count_pages += 1
        if is_published: count_pages_published += 1
        else: count_pages_drafts += 1
    else:
        count_posts += 1
        if is_published: count_posts_published += 1
        else: count_posts_drafts += 1

    add = post_add.get(pid, {})
    editor = add.get("_core", {}).get("editor")
    ext = {"markdown": "md", "tinymce": "html", "blockeditor": "json"}.get(editor, "txt")
    (target_dir / f"{slug}.{ext}").write_text(post["text"] or "", encoding="utf-8")

    author_ids = [int(a) for a in post["authors"].split(",") if a.strip()] if post["authors"] else []
    tag_ids = post_tags.get(pid, []) if not NO_TAGS else []

    metadata = {
        "title": post["title"],
        "status": post["status"],
        "template": post["template"],
        "created_at": post["created_at"],
        "modified_at": post["modified_at"],
        "authors": [author_map[aid] for aid in author_ids if aid in author_map],
        "tags": [tag_map[tid] for tid in tag_ids if tid in tag_map],
        "additional_data": add
    }

    has_featured = False
    if not NO_IMAGES and post["featured_image_id"] in images:
        img = images[post["featured_image_id"]]
        filename = os.path.basename(img["url"] or "")
        src = PROJECT_DIR / "media/posts" / str(pid) / filename
        dest = target_dir / f"{slug}.{Path(filename).suffix.lstrip('.')}"
        if filename and is_file(src):
            copyfile(src, dest)
            count_featured_images += 1
            has_featured = True
        elif img["url"]:
            count_featured_missing += 1
            missing_featured.append((slug, str(src)))
        metadata["featured_image"] = {
            "filename": filename,
            "title": img["title"],
            "caption": img["caption"],
            "additional_data": img["additional_data"]
        }

    num_inline = 0
    if not NO_IMAGES:
        inline_images = [img for img_id, img in images.items()
                         if img["post_id"] == pid and img_id != post["featured_image_id"] and img.get("url")]
        subdir = None
        for img in inline_images:
            filename = os.path.basename(img["url"] or "")
            src = PROJECT_DIR / "media/posts" / str(pid) / filename
            if not filename:
                continue
            if not subdir:
                subdir = target_dir / slug
                subdir.mkdir(exist_ok=True)
            dst = subdir / filename
            if is_file(src):
                copyfile(src, dst)
                count_inline_images += 1
                num_inline += 1
            else:
                count_inline_missing += 1
                missing_inline.append((slug, str(src)))
            write_json(subdir / f"{filename}.metadata.json", img)

    write_json(target_dir / f"{slug}.metadata.json", metadata)

    emoji = "📄" if is_page else "📝"
    suffix = ""
    if num_inline or has_featured:
        parts = []
        if num_inline:
            parts.append(str(num_inline))
        if has_featured:
            parts.append("+1")
        suffix = f" ({''.join(parts)})"
    print(f"{emoji} {type_dir}/{status_dir}/{slug}.{ext}: {post['title']}{suffix}")

# Summary
print("\n📦 Summary:")
if not NO_AUTHORS:
    print(f"  👤 Authors exported: {count_authors}")
if not NO_TAGS:
    print(f"  🏷️    Tags exported: {count_tags}")
print(f"  📝   Posts exported: {count_posts} (🟢 published: {count_posts_published}, 🟡 drafts: {count_posts_drafts})")
print(f"  📄   Pages exported: {count_pages} (🟢 published: {count_pages_published}, 🟡 drafts: {count_pages_drafts})")
if not NO_IMAGES:
    print(f"  🖼️  Featured images copied: {count_featured_images} (missing: {count_featured_missing})")
    print(f"  🖼️    Inline images copied: {count_inline_images} (missing: {count_inline_missing})")
    if missing_featured:
        print("\n🚫 Missing featured images:")
        for slug, path in missing_featured:
            print(f"  - {slug} → {path}")
    if missing_inline:
        print("\n🚫   Missing inline images:")
        for slug, path in missing_inline:
            print(f"  - {slug}/{os.path.basename(path)} → {path}")
