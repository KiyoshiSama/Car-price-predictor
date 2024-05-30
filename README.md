# Car Price Predictor
## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#licence)
- [Contact](#contact)

## Project Overview

Car Price Predictor is a machine learning project that aims to predict the prices of cars based on their information on [bama](https://bama.ir) website. The project includes data preprocessing, model training, evaluation, and prediction components, designed to provide accurate and reliable car price predictions.

There are two folders in the project, the one with *all_cars* name retrives the data of all cars appearing in website page. Because the websites loads data dynamically, there is a window.scrollby() function which scrolls the page only for 1000 pixels. You can change the value with your choice.

There is also another folder with the name *pride_and_207* which only captures data of the specified cars pride and 207.

You can specify your desired car model in predict scripts.

for the *all_cars* prediction script, you can specify any car name you want. but the data is inaccurate.
for the *pride_and_207* prediction script, you can specify the pride model you want (صندوق دار،111،131). 


## Installation

To set up the project locally, follow these steps:

```bash 
git clone https://github.com/KiyoshiSama/Car-price-predictor.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```
## Usage

Run the fetching script:
```
python3 fetch_all_cars.py
```
It will return a csv file which contains the information about all the new listed cars in [bama](https://bama.ir) website.

Run the prediciting script: **(Be sure to double check the path of csv file in the script because output of the file depends on this!)**
```bash
python3  predict_cars_pricee.py
```
## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit them:
```bash
git commit -m 'Add some feature'
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a pull request.

## Licence

This project is licensed under the MIT License. See the [LICENSE](LICENCE.txt) file for details.

## Contact
- **GitHub:** [KiyoshiSama](https://github.com/KiyoshiSama)
- **Email:** [awmiirh@gmail.com](mailto:awmiirh@gmail.com)