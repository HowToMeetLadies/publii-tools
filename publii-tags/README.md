# publii-tags

🏷️ A Python tool to manage post tags in [Publii](https://getpublii.com/) sites.

**Version:** 0.1.0  
**License:** GPLv3  
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## ⚠️ Warning

This tool works **directly on the Publii database** (`db.sqlite`).  
If used incorrectly, it may modify or delete tag relations in your posts.

> Always create a **backup of your database** before using this tool.  
> The author assumes **no responsibility** for data loss or corruption.

---

## ✨ Features

- List tags of one or multiple posts
- Add new tags to posts (`--append`)
- Replace all tags in posts (`--replace`)
- Remove all tags from posts (`--clear`)
- Apply to specific post IDs or all posts
- Validates all provided tag slugs before applying changes
- Supports both space-separated and comma-separated tag input

---

## 📦 Installation

Copy the `publii-tags` script to your tool directory and make it executable:

```bash
chmod +x publii-tags
```

---

## 🚀 Usage

```bash
./publii-tags <PATH_TO_DB> [OPTIONS] [TAGS...]
```

`<PATH_TO_DB>` must be the full path to the `db.sqlite` file of your Publii site.  
Example: `~/Documents/Publii/sites/mysite/input/db.sqlite`

---

## 🛠 Options

| Option           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `--append`       | ➕ Add tags to selected posts (existing ones remain)                         |
| `--replace`      | ♻️ Replace all tags in selected posts with the given tags                   |
| `--clear`        | 🧹 Remove all tags from selected posts                                       |
| `--post-ids`     | 🔢 Comma-separated list of post IDs (e.g. `5,7,8`)                           |
| `--all`          | 📌 Apply to all posts in the database                                        |
| `--help`         | 📖 Show help and usage                                                       |

If **none** of `--append`, `--replace`, or `--clear` is used,  
the default action is `--list`, which prints tags for each post.

---

## 🔍 Examples

### List tags of post 5 and 6

```bash
./publii-tags ~/Documents/Publii/sites/mysite/input/db.sqlite --post-ids 5,6
```

### Append tags using comma-separated input

```bash
./publii-tags ~/Documents/Publii/sites/mysite/input/db.sqlite --append --post-ids 10 "tech,news"
```

### Append tags using separate arguments

```bash
./publii-tags ~/Documents/Publii/sites/mysite/input/db.sqlite --append --post-ids 10 tech news
```

### Replace all tags in post 12

```bash
./publii-tags ~/Documents/Publii/sites/mysite/input/db.sqlite --replace --post-ids 12 featured,update
```

### Remove all tags from all posts

```bash
./publii-tags ~/Documents/Publii/sites/mysite/input/db.sqlite --clear --all
```

---

## 🔐 Tag Validation

All tag slugs must already exist in the database.  
If one or more slugs do not exist, the tool will abort with an error:

```
❌ The following tags do not exist in the database: unknown-tag,invalid
```

---

## ✅ Requirements

- Python 3.6+
- Compatible with Linux, macOS, WSL

---

## 📜 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit:  
[https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 🤝 Contributions

Issues, suggestions and pull requests are welcome!

> `publii-tags` is part of [publii-tools](https://github.com/HowToMeetLadies/publii-tools)
