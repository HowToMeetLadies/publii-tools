# publii-check

🧪 A diagnostic and sandbox inspection tool for [Publii](https://getpublii.com/) on Linux systems.

**Version:** 0.3.0
**License:** GPLv3
**Author:** [HowToMeetLadies](https://github.com/HowToMeetLadies)

---

## 🎯 Purpose

`publii-check` is a read-only shell script designed to:

* Inspect the host system for compatibility with Publii
* Detect whether Publii is running in a sandbox (Snap, Flatpak, Bubblewrap)
* Show hardware and environment details (CPU, OS, DE, WM, virtualization)
* Identify the installation type (AppImage, DEB, RPM)
* Verify Electron sandbox compatibility (`chrome-sandbox` permissions)
* Report checksums for binaries and installer files
* Assist in process launching or selection
* Output complete environment variables for the Publii process

---

## ✅ Features

* Fully portable Bash script (POSIX + coreutils)
* **Does not modify the system** (read-only: no chmod, no writes)
* Compatible with X11 and Wayland
* Detects Electron sandbox readiness
* Interactive launch & analysis options

---

## 🛠️ Usage

```bash
chmod +x publii-check
./publii-check
```

You’ll be guided through the checks and optionally prompted to launch Publii.

---

## 🛠️ Requirements

* Bash (4.x+)
* Standard GNU/Linux (core) utilities: `ps`, `grep`, `stat`, `awk`, `tr`, `find`, etc.
* No root access required

---

## 🔒 License

This project is licensed under the GNU General Public License v3.0.
See the [LICENSE](./LICENSE) file or visit [gnu.org/licenses](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🤝 Contributions

Suggestions, issues or pull requests are welcome!

> publii-check is part of [publii-tools](https://github.com/HowToMeetLadies/publii-tools)
