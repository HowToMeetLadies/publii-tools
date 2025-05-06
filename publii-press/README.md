# publii-press

📤 A Python tool to convert a WXR file into a [Publii](https://getpublii.com/) static site project.

**Version:** 0.1.0a
**License:** GPLv3
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## ⚠️ Warning - ALPHA RELEASE

This tool works **directly on the Publii sites directory** (`sites`).  
If used incorrectly, it may modify or corrupt your content.

> Always create a **backup** before using this tool.  
> The author assumes **no responsibility** for data loss.

> 🧠 **Important:** Your Publii project **must contain exactly one author**,  
> and their name **must not appear** in the WXR export file.  
> Otherwise, the import will be aborted.

---

## ✨ Features

- Converts WordPress WXR export files into Publii site content
- Supports import of:
  - Authors
  - Tags and categories (categories are imported as tags prefixed with `category-`)
  - Posts
  - Pages
  - Featured and inline media
- Handles image name conflicts with user interaction (`re-use`, `overwrite`, `rename`, `abort`)
- Automatically detects missing file extensions by MIME type
- Downloads and stores images into correct media paths
- Generates `pages.config.json`
- Offers dry-run mode for safe testing

---

## 📦 Installation

```bash
chmod +x publii-press
pip install lxml
```

---

## 🚀 Usage

```bash
./publii-press [OPTIONS] <WXR_FILE> <PATH_TO_DB>
```

**Example:**

```bash
./publii-press export.xml ~/Documents/Publii/sites/mysite/input/db.sqlite
```

---

## 🛠 Options

| Option         | Description                                                    |
|----------------|----------------------------------------------------------------|
| `--help`       | Show help and usage                                            |
| `--version`    | Show tool version                                              |
| `--verbose`    | Print detailed import information                              |
| `--dry-run`    | Simulate import, no changes to filesystem or database          |
| `--no-authors` | Skip importing authors                                         |
| `--no-tags`    | Skip importing tags and categories                             |
| `--no-media`   | Skip downloading media (featured and inline)                   |
| `--no-pages`   | Skip importing WordPress pages                                 |
| `--no-posts`   | Skip importing WordPress posts                                 |

---

## 🔍 Example Workflow

1. Create a new Publii site via the app
2. Choose a dummy author name (e.g. `fallback`) – it **must not** exist in WXR
3. Export your WordPress site as WXR (XML) file
4. Run:

```bash
./publii-press blog-export.xml ~/Documents/Publii/sites/mysite/input/db.sqlite
```

5. Open the site in Publii – your content is now imported 🎉

---

## ✅ Requirements

- Python 3.7+
- `lxml`
- Compatible with Linux, macOS, WSL

---

## 📜 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit:  
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 🤝 Contributions

Pull requests and issue reports are welcome!

Part of the [publii-tools](https://github.com/HowToMeetLadies/publii-tools) suite.
