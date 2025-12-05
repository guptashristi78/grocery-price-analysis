# Grocery Price Analysis Project

This project generates a sample dataset of grocery prices for multiple items,
across different stores and months. It then performs data analysis and 
visualization to find:

- Cheapest store for each item  
- Monthly inflation trend  
- Price stability (Mean, STD, Variance)  
- Item-wise price comparison across stores  
- Overall best (cheapest) store  

## 📁 Project Structure
grocery-price-analysis/
│
├── README.md               ← Project documentation (this file)
├── requirements.txt        ← Python dependencies
├── data_generation.py      ← Generates dataset (grocery_prices.csv)
├── analysis.py             ← Performs analysis + saves graphs
├── grocery_prices.csv      ← Auto-created after running data_generation.py
└── plots/                  ← Automatically created folder for graphs
