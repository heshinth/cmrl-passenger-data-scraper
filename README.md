# CMRL Passenger Flow Data Scraper

![GitHub License](https://img.shields.io/github/license/heshinth/cmrl-passenger-data-scraper?cacheSeconds=30)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)

A Python-based scraper that automatically collects daily passenger flow data from Chennai Metro Rail Limited (CMRL).

## Overview

This project scrapes passenger data from [CMRL's Passenger Flow Portal](https://commuters-data.chennaimetrorail.org/passengerflow) and stores it in CSV format. The data includes:

- Hourly passenger counts
- Station-wise passenger flow for Line 1 and Line 2
- Ticket type distribution statistics

## Data Collection

- Data is scraped automatically at 12:15 AM IST daily using GitHub Actions
- Historical data available from January 20, 2025
- Data is stored in the `data/` directory in CSV format:
  - `passenger_flow_hourly.csv`: Hourly passenger counts
  - `passenger_flow_line_01.csv`: Line 1 station-wise data
  - `passenger_flow_line_02.csv`: Line 2 station-wise data
  - `passenger_ticket_count.csv`: Daily ticket type statistics
- For more details check [here](data/README.md)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/heshinth/cmrl-passenger-data-scraper.git
cd cmrl-passenger-data-scraper
```

2. Install dependencies using `uv`:

   ```bash
   uv sync --all-extras
   ```

3. Run the scraper manually:
   ```
   python main.py
   ```

## Todo

- [ ] Add JSON schema validation for API response changes
- [ ] Add data validation checks
- [ ] Add API documentation
- [ ] Implement error notification system

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For any inquiries or issues, please open an issue on the [GitHub repository](https://github.com/heshinth/cmrl-passenger-data-scraper/issues).

## Disclaimer

- This project scrapes data directly from the CMRL's passenger flow portal
- The data is provided "**as is**" without any guarantees of accuracy or completeness
- This is an **unofficial** tool and not affiliated with CMRL
- The scraping process may be affected by changes to CMRL's website structure

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---