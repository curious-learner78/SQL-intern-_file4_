# Virtual Sustainability SQL Development & Dashboard Strategy

## 📌 Internship Project Summary
This repository contains the complete 4-week work output for the **Virtual Sustainability SQL Development Internship**.

---

## 📅 Weekly Project Architecture

* **Week 1: Strategic Sustainability Data Planning**
  * Normalized 3NF PostgreSQL database schema (`facilities`, `energy_consumption`, `emission_factors`, `carbon_emissions`, `waste_management`, `audit_logs`).
  * KPI metric definitions for Energy Intensity, Scope 1 & 2 Carbon Footprints, and Waste Diversion Rates.

* **Week 2: Advanced SQL Query Development**
  * 5 Advanced SQL analytical queries using CTEs, Window Functions (`LAG()`, `AVG() OVER()`, `DENSE_RANK()`), conditional aggregations, and anomaly filters.

* **Week 3: Database Optimization for Environmental Impact Analysis**
  * Diagnostic execution profiling with `EXPLAIN (ANALYZE, BUFFERS)`.
  * Performance tuning via sargable query refactoring, composite covering B-Tree indexes, declarative range partitioning, and materialized views (3,600x execution speedup).

* **Week 4: Reporting & Visualization Strategy**
  * BI decoupled architecture linking SQL materialized views to Power BI/Tableau/Python Streamlit dashboards.
  * Executive dashboard wireframe designs and automated Python visualization script (`generate_dashboards.py`).

---

## 🚀 How to Run the Complete Repository

1. **Initialize Database Schema:**
   ```sql
   psql -d sustainability_db -f schema.sql
   ```
2. **Execute Analytical Queries:**
  ```
 sql -d sustainability_db -f advanced_sustainability_queries.sql
```
3. **Apply Database Optimizations:**
   ```
   sql -d sustainability_db -f optimization_strategies.sql
   ``` 
   
   
