1. **Key Metrics Summary (Scorecards & KPIs)**

    📊 **Implementation:**
    - Add a Scorecard for each metric:
      - Select Scorecard from the chart options.
      - Set Metric:
         - Total Crimes: `SUM(crime_count)`
         - Average Crimes Per Day: `avg_crimes_per_day`
         - Crime Density: `crime_density`
         - Crime Score: `crime_score`
      - Use Conditional Formatting:
         - Green for low crimes, Red for high crimes.
      - Add Trend Indicators:
         - Compare with previous month (`pct_change_avg_crimes_per_day_by_area`).

2. **Crime Trends & Analysis (Line/Bar Charts)**

    📈 **Implementation:**
    - Add a Line Chart (Monthly Trends)
      - Dimension: `datemon_occ`
      - Metric: `SUM(crime_count)`
      - Style: Enable “Smooth lines” and add trendlines.
    - Add a Bar Chart (Crime Rate Change by Area)
      - Dimension: `area_name`
      - Metric: `pct_change_avg_crimes_per_day_by_area`
      - Color Encoding: Green for decrease, Red for increase.
    - Add a Table (Top 10 Areas by Crime Rate Change)
      - Columns: `area_name`, `pct_change_avg_crimes_per_day_by_area`
      - Sorting: Descending by percentage change.

3. **Geographic Crime Distribution (Maps & Heatmaps)**

    🌍 **Implementation:**
    - Add a Google Maps Chart (Crime Hotspots)
      - Latitude: `lat`
      - Longitude: `lon`
      - Metric: `SUM(crime_count)`
      - Size By: `crime_score`
      - Color By: `crime_density` (High = Red, Low = Green).
    - Add a Geo Heatmap (Crime Scores by Area)
      - Dimension: `geo_display_name`
      - Metric: `crime_score`
      - Color Gradient: Blue (Low) to Red (High).

4. **Crime Demographics & Correlations (Bar & Scatter Plots)**

    👥 **Implementation:**
    - Add a Bar Chart (Crime Count by Age Group)
      - Dimension: `vict_age_group`
      - Metric: `SUM(crime_count)`
    - Add a Scatter Plot (Crime Correlation by Age)
      - X-Axis: `corr_crime_count_age_group`
      - Y-Axis: `crime_count`
      - Size By: `crime_score_by_age_group`
      - Color: Gradient from Blue (Weak Correlation) to Red (Strong Correlation).
    - Add a Table (Correlation Strength)
      - Columns: `vict_age_group`, `corr_crime_count_age_group_strength`.

5. **Crime Type Breakdown (Ranked Tables & Heatmaps)**

    ⚖ **Implementation:**
    - Add a Bar Chart (Top 10 Crime Types)
      - Dimension: `crm_cd_desc`
      - Metric: `SUM(crime_count)`
      - Sorting: Descending by count.
    - Add a Heatmap (Crime Type vs Area)
      - Rows: `crm_cd_desc`
      - Columns: `area_name`
      - Metric: `crime_score_by_crmcd`
      - Color Gradient: Light Blue (Low) to Dark Red (High).
    - Add a Table (Crime Scores by Type)
      - Columns: `crm_cd_desc`, `crime_score_by_crmcd`
      - Sorting: Descending by crime score.

🔹 **Enhancements & Best Practices**

    ✅ **Filters:**
    - Add Drop-down filters for:
      - `dateyear_occ`, `datemon_occ`
      - `area_name`
      - `crm_cd_desc`
      - `vict_age_group`
    - Enable “Apply Filters” button.

    ✅ **Drill-Downs:**
    - Enable Drill-down on Charts (e.g., Clicking an area zooms into crime types).

    ✅ **Performance Optimization:**
    - Use pre-aggregated data (BigQuery or optimized Sheets).
    - Avoid too many blended sources unless necessary.
