# web-button-clicker

Simple tool to automate clicking of a button of a specified website to download a file.

### Installation
1. Clone this repository and create python virtual environment in the root of the repository folder. Assuming you are using Linux, creating the python virtual environment is done with `python -m venv venv`
2. Open the python venv. `source venv/Scripts/activate`
3. Install dependencies with `pip install -r requirements.txt`

### Command
- If you are in the python environment of this folder, do `python downloader.py <options>`
- If you are using this as a cron/automation script, make sure your bash script either:
    1. includes `source venv/Scripts/activate` before running downloader.py
    2. run downloader.py from outside the python virtual environment with `./venv/Scripts/python downloader.py <options>

### Options

| Options       | Description                                                  | Optional? | Default value |
| ------------- | ------------------------------------------------------------ | --------- | ------------- |
| -h, --help    | show this help message and exit.                             | -         | -             |
| --url         | Enter URL of website with button to click.                   | Required  | -             |
| --buttonclass | Enter a unique classname of HTML element of button to click. | Required  | -             |
| --target      | Enter relative file location to download file to.            | Optional  | downloads     |
| --filename    | Enter filename to save as.                                   | Optional  | downloadfile  |
| --timeout     | Enter timeout for downloading file .                         | Optional  | 20            |

### Example

`python3 downloader.py --url=https://www.youtube.com/ --target=videos --buttonclass=12345 --filename=new-video`

Opens Chrome browser at YouTube main page, clicks on a HTML element with class of `12345`, downloads a file to `videos` folder (relative to script location) and renames this downloaded file as `new-video`.
