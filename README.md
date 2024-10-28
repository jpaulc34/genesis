
# GENESIS

Project Genesis - Ordering System/POS and Inventory Management (API) built with FastAPI and MongoDB (PyMongo)

## Features

- Product Management
- Inventory Management (stock checks, updates, and alerts)
- Order Management (Order summary reports, including customer-specific orders)
- Customer Management
- User and Team Management
- Deployment Management (Real-time deployment tracking and status management)
- Sales and Financial Reporting

## Technologies Used

- **FastAPI**: Asynchronous web framework for building APIs
- **MongoDB**: Document-Based database
- **Docker**: Containerization platform
- **Pydantic**: Data validation and settings management

## Setup Instructions

### Prerequisites

- Ensure you have [Docker](https://www.docker.com/get-started) installed on your machine.
- Install [Python 3.12.7](https://www.python.org/downloads/) or higher.
- Install [Make 3.81](via homebrew) or higher.

### Running the Application

#### Docker setup - MAC

```bash
make build-up
