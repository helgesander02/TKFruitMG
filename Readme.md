# management_system

* figma : https://www.figma.com/file/HOM1DRGSk0ZzpSYHd4wj4s/%E6%B0%B4%E6%9E%9C%E5%BA%97?type=design&node-id=0-1&t=jJ842c2FEezbnEHB-0

## Installation

* Clone this repo by `git clone https://github.com/helgesander02/TKFruitMG`
* Python libraries. Install core requirements by `pip install -r requirements.txt`

## Packaging

* tkcalendar Error: https://github.com/j4321/tkcalendar/issues/79#issuecomment-1509958936
* Packaging: `pyinstaller --noconfirm --onedir --windowed --add-data "<path to python>\Lib\site-packages\customtkinter;customtkinter/" --add-data "<path to python>\Lib\site-packages\tkcalendar;tkcalendar/" --add-data "<path to python>\Lib\site-packages\babel;babel/"  "C:\Users\helge\OneDrive\桌面\Fruit\home.py"`

## TODO
□ Copy 備份到雲端 <br />
□ 列印 <br />

□ 銷貨單編號是可以不用TAB就改變 <br />
□ 刪除明細不會更新 <br />
□ 新增銷貨單，離開的時候沒有存檔確認不小心按到離開就要全部重打 <br />
□ 入賬按返回會離開查詢的對象，要重查 <br />
□ 按下確認入帳不會跳通知或跳出，不知道到底有沒有入到 <br />
□ 輸入銷貨單的時候沒辦法用上下鍵換格子嗎? <br />