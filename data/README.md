# CMRL Passenger Data Documentation

This folder contains CSV datasets with passenger flow statistics from Chennai Metro Rail Limited (CMRL). The data is updated daily through automated scraping using Github Actions.

## Available Datasets

### 1. passenger_flow_hourly.csv

Contains hourly passenger counts across the entire metro system.

**Columns:**

- `date_and_time`: Timestamp in UTC
- `Total`: Total passenger count
- Payment method breakdowns:
  - `Store Value Card`
  - `Token`
  - `Trip Card`
  - `Tourist Card`
  - `Group Ticket`
  - `NCMC Card`
  - `Paper QR`
  - `Mobile QR`
  - Various QR payment methods (WhatsApp, Paytm, PhonePe, etc.)

### 2. passenger_flow_line_01.csv & passenger_flow_line_02.csv

Station-wise passenger flow data for Line 1 and Line 2 respectively.

**Columns:**

- `Date`: Date of record
- `Line`: Metro line number (1 or 2)
- `Station`: Station name
- `Total`: Total passenger count at station
- Same payment method breakdowns as hourly data

### 3. passenger_ticket_count.csv

Daily aggregated statistics for different ticket types.

**Columns:**

- `Date`: Date of record
- `totalTickets`: Total tickets issued
- Various ticket type counts:
  - `noOfSVC`: Store Value Cards
  - `noOfNCMCcard`: National Common Mobility Cards
  - `noOfMobileQR`: Mobile QR tickets
  - Payment platform specific QR codes
  - Other ticket categories

## Data Format

- All CSV files use UTF-8 encoding
- Dates in YYYY-MM-DD format
- Numeric columns contain integer values
- Missing values represented as 0

## Update Frequency

Data is updated daily at 12:15 AM IST through automated scraping.

## Notes

- Historical data available from January 20, 2025
- All passenger counts are entry-only statistics
- Station codes match official CMRL station codes
