# 🧰 publii-tools

A collection of tools and diagnostics for [Publii](https://getpublii.com/).

**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)  
**License:** GPLv3  
**Status:** Actively maintained

---

## 📦 Included Tools

### [`publii-check`](./publii-check)

A diagnostic and sandbox-inspection tool for Publii on Linux systems.  
Helps users verify installation integrity, environment compatibility, and sandbox status.

* Detects Publii installations (AppImage, DEB, RPM)
* Validates Electron sandbox (`chrome-sandbox` setuid)
* Detects Snap, Flatpak, and Bubblewrap isolation
* Displays hardware & system info (CPU, DE, WM, virt)
* Interactive Publii process handling & environment dump
* Read-only, side-effect free (no chmod, no writes)

👉 See the full documentation in [`publii-check/README.md`](./publii-check/README.md)

---

### [`publii-dump`](./publii-dump)

A Python-based export tool that extracts content and metadata from Publii projects.  
Useful for backups, migrations, or external processing of Publii sites.

* Exports posts and pages with status (published/drafts)
* Supports Markdown, WYSIWYG, and Block editors
* Preserves author and tag relationships
* Optionally includes featured and inline images (with metadata)
* Structured output with per-post metadata
* Reports missing images without failing

👉 See the full documentation in [`publii-dump/README.md`](./publii-dump/README.md)

---

### [`publii-clean`](./publii-clean)

🧼 A simple shell tool to clean up temporary directories in Publii sites.

* Removes build leftovers like `output/`, `preview/`, and `*-files` folders
* Supports dry-run and interactive confirmation
* Filtering by type: include/exclude specific folder categories
* Safe defaults: no destructive actions without confirmation

👉 See the full documentation in [`publii-clean/README.md`](./publii-clean/README.md)

---

### [`publii-shrink`](./publii-shrink)

🧹 A shell tool to detect and optionally delete unreferenced media files in Publii site projects.

* Scans `input/media/posts/<post_id>/` and compares filenames against the database
* Supports dry-run mode and safe deletion of files
* Optionally removes `responsive/` subfolders when appropriate
* Summarizes unreferenced file counts by post and in total
* Bash-only, minimal dependencies (`sqlite3`)

👉 See the full documentation in [`publii-shrink/README.md`](./publii-shrink/README.md)

---

### [`publii-tags`](./publii-tags)

🏷️ A Python CLI tool to list, add, replace, or clear tags from posts in a Publii database.

* Works directly on the `db.sqlite` file in a Publii site
* Supports `--append`, `--replace`, and `--clear`
* Default mode lists tags per post
* Operates on specific post IDs or all posts
* Validates tags and aborts if unknown slugs are passed

👉 See the full documentation in [`publii-tags/README.md`](./publii-tags/README.md)

---

### [`publii-press`](./publii-press)

📤 A Python tool to convert WordPress WXR exports into Publii-compatible projects.

* Imports authors, tags, categories, posts, and pages
* Downloads and assigns featured + inline media
* Maps categories as tags (`category-<slug>`) and links them as `mainTag`
* Automatically generates `pages.config.json`
* Supports `--dry-run` mode

👉 See the full documentation in [`publii-press/README.md`](./publii-press/README.md)

---

## 🔒 License

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🚧 Roadmap

More tools may follow...

Contributions welcome via PR or issue!
