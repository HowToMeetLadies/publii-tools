# publii-clean

🧹 A simple shell tool to clean up temporary directories in [Publii](https://getpublii.com/) sites.

**Version:** 0.1.0
**License:** GPLv3
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## ✨ Features

- Removes the following directories in each Publii site:
  - `output`
  - `preview`
  - `*-files`
- Supports dry-run and interactive modes
- Fine-grained filtering via include/exclude flags

---

## 📦 Installation

Copy the `publii-clean` script to your local tool directory and make it executable:

```bash
chmod +x publii-clean
```

---

## 🚀 Usage

```bash
./publii-clean [OPTIONS] <PUBLII_DIR>
```

`<PUBLII_DIR>` must point to your Publii root folder that contains the `sites/` directory.

---

## 🛠 Options

| Option               | Description                                             |
|----------------------|---------------------------------------------------------|
| `--output`           | Remove only `output` directories                        |
| `--preview`          | Remove only `preview` directories                       |
| `--deploy`           | Remove only `*-files` directories                       |
| `--no-output`        | Exclude `output` directories from cleanup               |
| `--no-preview`       | Exclude `preview` directories from cleanup              |
| `--no-deploy`        | Exclude `*-files` directories from cleanup              |
| `--dry-run`          | 🔍 Show what would be deleted, without deleting anything |
| `-i`, `--interactive`| ❓ Ask before cleaning each site                         |
| `--help`             | 📖 Show help and exit                                    |

---

## 🔍 Examples

### Clean everything (default)

```bash
./publii-clean /path/to/publii
```

### Dry-run, interactive

```bash
./publii-clean --dry-run --interactive /path/to/publii
```

### Only remove `output` and `preview` folders

```bash
./publii-clean --output --preview /path/to/publii
```

### Clean all except `preview`

```bash
./publii-clean --no-preview /path/to/publii
```

---

## 🧠 How filtering works

- If **any** of `--output`, `--preview`, or `--deploy` are used → only those are removed.
- If only `--no-*` options are used → everything is removed **except** the excluded types.
- If **no filtering options** are given → all types are removed.

---

## ✅ Requirements

- Bash 4+
- Works on Linux, macOS, and WSL
- No external dependencies
---

## 📜 License

This project is licensed under the GNU General Public License v3.0.  
See the [LICENSE](./LICENSE) file or visit [gnu.org/licenses](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🤝 Contributions

Bug reports, feature ideas, and pull requests are welcome!

> `publii-clean` is part of [publii-tools](https://github.com/HowToMeetLadies/publii-tools)
