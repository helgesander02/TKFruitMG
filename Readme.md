# management_system

* figma : https://www.figma.com/file/HOM1DRGSk0ZzpSYHd4wj4s/%E6%B0%B4%E6%9E%9C%E5%BA%97?type=design&node-id=0-1&t=jJ842c2FEezbnEHB-0

## Installation

* Clone this repo by `git clone https://github.com/helgesander02/TKFruitMG`
* Python libraries. Install core requirements by `pip install -r requirements.txt`

## Packaging

* tkcalendar Error: https://github.com/j4321/tkcalendar/issues/79#issuecomment-1509958936
* Packaging: `pyinstaller --noconfirm --onedir --windowed --add-data "<path to python>\Lib\site-packages\customtkinter;customtkinter/" --add-data "<path to python>\Lib\site-packages\tkcalendar;tkcalendar/" --add-data "<path to python>\Lib\site-packages\babel;babel/"  "C:\Users\helge\OneDrive\桌面\Fruit\home.py"`

## TODO

* Order 訂單編號根據時間變動
* Accounting 一次性輸入金額 選擇N筆訂單輸入金額直接更改
* Accounting 查詢後直接重設後再查詢
* Accounting 預設查詢日期2000年
* Accounting 沒寫客戶編號查詢全部
* Accounting 客戶編號案Enter也查詢
* into Acounting 上一頁到Accounting
* 明細單列印
