# management_system

* figma : https://www.figma.com/file/HOM1DRGSk0ZzpSYHd4wj4s/%E6%B0%B4%E6%9E%9C%E5%BA%97?type=design&node-id=0-1&t=jJ842c2FEezbnEHB-0

## Installation

* Clone this repo by `git clone https://github.com/helgesander02/TKFruitMG`
* Python libraries. Install core requirements by `pip install -r requirements.txt`

## Packaging

* tkcalendar Error: https://github.com/j4321/tkcalendar/issues/79#issuecomment-1509958936
* Packaging: `pyinstaller --noconfirm --onedir --windowed --add-data "<path to python>\Lib\site-packages\customtkinter;customtkinter/" --add-data "<path to python>\Lib\site-packages\tkcalendar;tkcalendar/" --add-data "<path to python>\Lib\site-packages\babel;babel/"  "C:\Users\helge\OneDrive\桌面\Fruit\home.py"`

## TODO

* Accounting 一次入帳後跟更新查詢
* order編輯
