# publii-dump

📤 A content and metadata export tool for [Publii](https://getpublii.com/) websites.

**Version:** 0.1.0  
**License:** GPLv3  
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## 🎯 Purpose

`publii-dump` is a Python-based CLI tool that extracts content, metadata, authors, tags, and images from a Publii project into a structured folder layout.

It is intended for:

* Backups, migrations, or external processing of Publii content
* Converting Publii sites into other formats
* Debugging and inspection of content structure
* Selective export of posts, pages, authors, tags and images

---

## ✅ Features

* Exports posts and pages, split by **published/draft** status
* Preserves author and tag relationships
* Extracts additional metadata and editor format
* Supports Markdown, TinyMCE (HTML), and blockeditor (JSON)
* Optionally includes **featured** and **inline** images with metadata
* Report missing images

---

## 🛠️ Usage

```bash
chmod +x publii-dump.py
./publii-dump.py /path/to/db.sqlite --output ./exported
```

Optional flags:

```bash
  --ids           Comma-separated list of post IDs to export
  --no-tags       Skip tag export
  --no-authors    Skip author export
  --no-images     Skip all image exports
```

Example:

```bash
./publii-dump.py ~/docs/Publii/sites/mysite/input/db.sqlite --output ./dump --no-images
```

---

## 📁 Output Structure

```text
output/
├── authors/            → JSON files per author
├── tags/               → JSON files per tag
├── posts/
│   ├── published/
│   │   ├── slug.md
│   │   └── slug.metadata.json
│   └── drafts/
├── pages/
│   ├── published/
│   └── drafts/
```

If images are included:

- Featured images are saved next to the content
- Inline images are saved in a subfolder: `slug/`
- Each image has an associated `filename.metadata.json`

---

## 🧰 Requirements

* Python 3.6+
* Standard Python libraries (`sqlite3`, `json`, `argparse`)
* No external dependencies

---

## 🔒 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit [gnu.org/licenses](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🤝 Contributions

Bug reports, feature ideas, and pull requests are welcome!

> `publii-dump` is part of [publii-tools](https://github.com/HowToMeetLadies/publii-tools)
