# publii-shrink

🧹 A Python-based tool to detect and optionally delete unreferenced media files in [Publii](https://getpublii.com/) sites.

**Version:** 0.3.6  
**License:** GPLv3  
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## ⚠️ Warning

This tool operates **directly on your Publii project directory** (`input/` folder).  
If misconfigured, it may irreversibly delete media files.

> Always make a backup before using this tool with `--delete`.  
> The author accepts **no liability** for data loss or project damage.

---

## ✨ Features

- Scans a single Publii project directory
- Detects files in `input/media/posts/<post_id>/` that are **not referenced** in the database:
  - via `posts_images.url`
  - via `#DOMAIN_NAME#filename.ext` in `posts.text`
- Supports dry-run and deletion modes
- Handles `responsive/` subfolders:
  - Delete only if others are removed (`--responsive`)
  - Always delete (`--force-responsive`)
- Summarizes changes per post and in total

---

## 📦 Installation

Place `publii-shrink` into your tool path and make it executable:

```bash
chmod +x publii-shrink
```

It requires Python 3.6+ and standard libraries.

---

## 🚀 Usage

```bash
./publii-shrink [OPTIONS] <PROJECT_DIR>
```

`<PROJECT_DIR>` must point to a single Publii project folder  
(e.g. `~/Documents/Publii/sites/mysite`)

---

## 🛠 Options

| Option               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `--dry-run`          | 🔍 Show which files would be deleted (default)                              |
| `--delete`           | 🗑️  Actually delete unreferenced files                                      |
| `--responsive`       | 🧹 Delete `responsive/` folder only if other files in the same post are deleted |
| `--force-responsive` | 🔥 Always delete `responsive/`, even if no other files are deleted          |
| `--help`             | 📖 Show help and exit                                                        |

---

## 🔍 Examples

Dry-run (default):

```bash
./publii-shrink ~/Documents/Publii/sites/my-site
```

Delete unreferenced files:

```bash
./publii-shrink --delete ~/Documents/Publii/sites/my-site
```

Delete files and responsive folders if needed:

```bash
./publii-shrink --delete --responsive ~/Documents/Publii/sites/my-site
```

Always delete responsive folders:

```bash
./publii-shrink --delete --force-responsive ~/Documents/Publii/sites/my-site
```

---

## 🧠 Behavior Details

- Only files inside `input/media/posts/<post_id>/` are considered
- Referenced media includes:
  - Filenames in `posts_images.url`
  - Filenames embedded via `#DOMAIN_NAME#filename` in `posts.text`
- The tool compares **plain filenames**, not full paths
- Responsive folders are excluded unless:
  - `--responsive` is given **and** other files are deleted
  - `--force-responsive` is given
- If both `--dry-run` and `--delete` are passed, dry-run takes precedence

---

## ✅ Requirements

- Python 3.6+
- No third-party libraries required
- Works on Linux, macOS, and WSL

---

## 📜 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit:  
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 🤝 Contributions

Pull requests, bug reports, and suggestions welcome!

> `publii-shrink` is part of the [publii-tools](https://github.com/HowToMeetLadies/publii-tools) collection.
