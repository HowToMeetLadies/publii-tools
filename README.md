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

## 🔒 License

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🚧 Roadmap

More tools may follow..

Contributions welcome via PR or issue!
