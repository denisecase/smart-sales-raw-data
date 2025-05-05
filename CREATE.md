# Create Raw Data Files


## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux). 

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.
Verify that all external packages imported into a file are included in requirements.txt (and have NOT been commented out).

```shell
py create.py
```

## CheatSheet: Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```
