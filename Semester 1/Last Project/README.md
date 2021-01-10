# Invest Mart

Invest Mart is like minimart but in this project have 2 role employee and administrator.

* For Administrator :
  * Add Product
  * Update Product (update stock and price product)
  * Delete Product
  * Buyer's Shopping Rreport

* For Employee :
  * Add Shopping Products
  * Delete Shopping Products
  * Pay for Shopping


## Directory

* `data.json` - Data Storage
* `main.json` - Main Program Code
* `module.json` - Module program to save data

## Usage
1. Run `main.py`

2. Login or Register

Register for employee and doesn't have register for Administrator so you can add manual to `data.json` with status `1` for Administrator.

Username  | Password | Status role
------------ | -------------  | -------------
admin | admin | Administrator
employee | employee | Employee

If you want add product, update product and delete product you can login with role Administrator.

If you want add shopping product for buyer's you can login with role Employee.

## License
[MIT](https://choosealicense.com/licenses/mit/)
