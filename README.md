<div id="top"></div>

# Portfolio-Optimization-on-Markowitz-Model-using-Hill-climbing-and-AMPO

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#set-up-environment">Set up Environment</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is a project to find out the best weighting of each shares in a portfolio with Sharp Ratio in a Markowitz Model using Hill-climbing and AMPO.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- SET UP ENVIRONMENT -->

## Set up Environment

```sh
conda env create --file environment.yml
```

<!-- USAGE EXAMPLES -->

## Usage

1. **Data Preparation**

   **1.1 Prepare `"./data/SharePrices_modified.csv"`:**\
    This csv file is the data of the stocks you hold within a duration.

   **1.2 Input necessary parameters in `"./params.py"`:**\
    Input parameters such as risk free rate, path of the data (stated in 1.1), bound, maximum iterations, step size, etc.

2. **Data Pre-processing**

   Run `"./main.py"` after deciding which of the following actions to take.

   **2.1 Use AMPO to find the best proportions:**\
    Uncomment `ampo(objective)` in `"./main.py"`

   **2.2 Use Hill Climbing to find the best proportions:**\
    Uncomment `hillClimb(objective)` in `"./main.py"`

   **2.3 Save the process data (if necessary):**\
    Uncomment `getData(input_sol)` in `"./main.py"`

   **2.4 Verify if the sum of weighting is 100% (if necessary):**\
    Uncomment `print("Total Percentage: %s%%" % (sum(input_sol)*100))` in `"./main.py"`

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Chun Kei Chan - [@gmail](chunkeichan1901@gmail.com)

Project Link: [https://github.com/chunkeichan/Portfolio-Optimization-on-Markowitz-Model-using-Hill-climbing-and-AMPO/](https://github.com/chunkeichan/Portfolio-Optimization-on-Markowitz-Model-using-Hill-climbing-and-AMPO/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

This project makes use of AMPO and hill climbing techniques in the following resources. Here, I would like to give credits to:

- [The Adaptive Multi-Population Optimization (AMPO) Algorithm](https://github.com/rayzxli/AMPO)
- [Iterated Local Search From Scratch in Python](https://machinelearningmastery.com/iterated-local-search-from-scratch-in-python/)

<p align="right">(<a href="#top">back to top</a>)</p>
