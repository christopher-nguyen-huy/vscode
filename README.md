# VSCode
## Panel prefixes
### Extensions:
- @installed
- @builtin
- @enabled
- @disabled
- @sort:rating
- @sort:installs

### Main popup
- `@`: symbols
- `@:`: symbols by type
- `>`: commands
- `?`: command suggestions
- `edt`: show open editors
- `>ext install`: search addons

## Shortcuts to memorize:
| Function | Shortcut |
| :- | :- |
| Theme selector | ctrl k ctrl t |
| Shortcut editor | ctrl k ctrl s |
| Git Panel | ctrl shift g |
| Addons Panel | ctrl shift a |
| Settings Panel | ctrl , |
| Zen Mode | ctrl k z |
| Toggle Activity Bar | ctrl k ctrl a |
| Fast scroll | alt scrollwheel |
| Format file (beautify) | ctrl shift i |
| Format selection | ctrl k ctrl f |
| Fold/Unfold | ctrl shift [/] |
| Select current line | ctrl l |
| Markdown Preview | ctrl shift v |
| Markdown Preview Edit | ctrl k v |
| Toggle terminal | ctrl ` |
| New terminal | ctrl shift ` |
| New split terminal | ctrl shift 5 |
| Navigate open terminals | alt left/right |
| Open external terminal | ctrl shift c |
| Add cursors by mouse | ctrl click |
| Insert line below | ctrl enter |
| Insert line above | ctrl shift enter |
| Toggle word wrap | alt z |
| Show all symbols | ctrl t |
| Go to definition | f12 |
| Peek definition | ctrl f12 |
| Code run | ctrl alt n |
| Code stop | ctrl alt m |
| Open intellisense | ctrl space |


## `if __name__ == '__main__':`
`main` is the snippet

## Workspaces
Workspace specific files are in a `.vscode` folder at the root. For example, `tasks.json` for the Task Runner and `launch.json` for the debugger.

## Debug file `launch.json`
- In `.vscode/launch.json`

## Settings file `settings.json`
- Exists in for user and in `.vscode/settings.json`
- May contain language specific settings for each
	```json
	{
		  "[typescript]": {
		    "editor.formatOnSave": true,
		    "editor.formatOnPaste": true
		  },
		  "[markdown]": {
		    "editor.formatOnSave": true,
		    "editor.wordWrap": "on",
		    "editor.renderWhitespace": "all",
		    "editor.acceptSuggestionOnEnter": "off"
		  }
	}
	```
## Extensions
### From cli
- `code --list-extensions`
- `code --install-extension <extension-id>`

### From command pallete
- `ext install <extension-id>`


## Keybindings file `keybindings.json`
- Needed to add [multiple shortcuts to 1 command](https://stackoverflow.com/a/45384050)

## Not working!
- [ctrl alt (num|arrow) shortcuts](https://github.com/Microsoft/vscode/issues/68787)
	- want to use for move editor
- [right click manipulation](https://github.com/Microsoft/vscode/issues/3130)
- Advanced new file doesn't autocomplete, project abandoned [issue 426](https://github.com/Microsoft/vscode/issues/426)