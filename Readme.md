# management_system

* figma : https://www.figma.com/file/HOM1DRGSk0ZzpSYHd4wj4s/%E6%B0%B4%E6%9E%9C%E5%BA%97?type=design&node-id=0-1&t=jJ842c2FEezbnEHB-0

## Installation

* Clone this repo by `git clone https://github.com/helgesander02/TKFruitMG`
* Python libraries. Install core requirements by `pip install -r requirements.txt`

## Packaging

* tkcalendar Error: https://github.com/j4321/tkcalendar/issues/79#issuecomment-1509958936
* Packaging: `pyinstaller --noconfirm --onedir --windowed --add-data "<path to python>\Lib\site-packages\customtkinter;customtkinter/" --add-data "<path to python>\Lib\site-packages\tkcalendar;tkcalendar/" --add-data "<path to python>\Lib\site-packages\babel;babel/"  "C:\Users\helge\OneDrive\桌面\Fruit\home.py"`

## TODO

□ Copy 備份到雲端
1.品項/客戶管理的編輯很不方便，要先按查詢才會出來
沒辦法直接編輯，然後也沒辦法刪除
2.新增銷貨單，離開的時候沒有存檔確認
不小心按到離開就要全部重打
3.銷貨單換劣勢tab，換行的時候卻變成enter，按tab游標還會消失
4.在金額或數量的地方tab2次，下一行的內容會重複
5.輸入銷貨單的時候沒辦法用上下鍵換格子嗎?
6.沒辦法刪除明細
7.新增銷貨單只能打完一個人後跳出重開?
8.明細打到最後一列，不按enter到下一列的話按存檔不會儲存
9.銷貨單輸入的頁面，按查詢會不知道哪幾筆是誰的
10.銷貨單編輯那邊，更改金額或數量，小計不會跟著改
11.刪除銷貨單的時候要跳確認視窗
12.銷貨單頁面要有各銷貨單的小計
13.入帳的部分，那個未按下enter的問題
14.按下確認入帳不會跳通知或跳出，不知道到底有沒有入到
15.入賬按返回會離開查詢的對象，要重查
16.列印的格式
17.列印頁面查詢完跳出會有bug