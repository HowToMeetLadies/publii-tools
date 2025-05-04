# publii-shrink

🧹 A shell tool to detect and optionally delete unreferenced media files in [Publii](https://getpublii.com/) sites.

**Version:** 0.1.0  
**License:** GPLv3  
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## ⚠️ Warning

This tool operates **directly on the `input/` folders** of your Publii sites.  
If a bug or misconfiguration occurs, it may delete media files irreversibly.

> Always make sure you have a **current backup** of your project before using this tool with `--delete`.  
> I accept **no responsibility** for any damage or data loss – **you have been warned**.

---

## ✨ Features

- Scans all sites under `sites/*` in your Publii root directory
- Detects files in `input/media/posts/<post_id>/` that are **not referenced** in the database (`posts_images.url`)
- Supports dry-run and actual deletion modes
- Handles `responsive/` subfolders:
  - Delete only if needed (`--responsive`)
  - Always delete (`--force-responsive`)
- Outputs a summary with per-post file counts and a total

---

## 📦 Installation

Copy the `publii-shrink` script to your local tool directory and make it executable:

```bash
chmod +x publii-shrink
```

---

## 🚀 Usage

```bash
./publii-shrink [OPTIONS] <PUBLII_DIR>
```

`<PUBLII_DIR>` must be the root of your Publii project (i.e. the directory containing `sites/`).

---

## 🛠 Options

| Option               | Description                                                                  |
|----------------------|------------------------------------------------------------------------------|
| `--dry-run`          | 🔍 Show which files would be deleted, without deleting anything (default)    |
| `--delete`           | 🗑️  Actually delete unreferenced files                                       |
| `--responsive`       | 🧹 Delete `responsive/` folder only if other files in that post are deleted   |
| `--force-responsive` | 🔥 Always delete the `responsive/` folder, even if nothing else is deleted    |
| `--help`             | 📖 Show help and exit                                                         |

---

## 🔍 Examples

### Just show what would be deleted (default)

```bash
./publii-shrink /path/to/publii
```

### Delete unreferenced files

```bash
./publii-shrink --delete /path/to/publii
```

### Delete files and only clean `responsive/` if needed

```bash
./publii-shrink --delete --responsive /path/to/publii
```

### Always remove `responsive/` folders, even if nothing else is deleted

```bash
./publii-shrink --delete --force-responsive /path/to/publii
```

---

## 🧠 Behavior Details

- Only files in `input/media/posts/<post_id>/` are checked
- Referenced filenames are taken from the `posts_images.url` column (no subpath)
- `responsive/` folders are ignored unless:
  - `--responsive` is passed **and** other files in the post are deleted
  - or `--force-responsive` is passed
- If both `--dry-run` and `--delete` are given, `--dry-run` wins

---

## ✅ Requirements

- Bash 4+
- SQLite3 CLI (`sqlite3`)
- Compatible with Linux, macOS, and WSL

---

## 📜 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit:  
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 🤝 Contributions

Bug reports, improvements, and pull requests are welcome!

> `publii-shrink` is part of [publii-tools](https://github.com/HowToMeetLadies/publii-tools)
