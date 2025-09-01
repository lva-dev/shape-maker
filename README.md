# Shape Maker
Draw stuff!
## Building and Running
(Optional) Create and activate a Python venv (and activating it):<br>
*Example in Bash:*
```bash
python -m venv .venv
chmod +x .venv/bin/activate
. .venv/bin/activate
```
Then install the dependencies:
```bash
pip install pygame-ce numpy
```
*Note:* On some platforms, Tkinter doesn't come with Python, so you may need to install it manually.<br>
*Example on archlinux:*
```bash
sudo pacman -S tk
```
Now you can run Shape Maker `shape-maker.py` directly:
```
python shape-maker.py
```
## Controls
- `esc`: Open menu
- `mouse1` while dragging: Place/delete shapes
- `shift` + `mouse1` while dragging: Regularize drag
- `mouse2` while dragging: Cancel drag
- `1` to `7`, `scroll`, `mouse1` on hotbar: Change active tool/shape
- `mouse1` while dragging slider: Change active hue/saturation/value
- `shift` + `scroll`: Change active shape hue
- `R`: Clear canvas
## License
Shape Maker is distributed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.