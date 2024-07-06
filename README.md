# web-button-clicker

Simple tool to automate clicking of a button of a specified website to download a file.

`python3 downloader.py <options>`

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
